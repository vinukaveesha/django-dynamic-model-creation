from django.db import connections, models
from .admin import register_dynamic_model
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps
import logging

# Get the logger specified in settings
logger = logging.getLogger('model_creation_logger')

def create_all_dynamic_models(db_alias, schema_name):
    connection = connections[db_alias]
    tables = []

    with connection.cursor() as cursor:
        if db_alias == 'oracle':
            cursor.execute(f"SELECT table_name FROM all_tables WHERE owner = '{schema_name}'")
        else: 
            cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema_name}'")

        tables = [row[0] for row in cursor.fetchall()]

    for table_name in tables:
        logger.debug(f"Starting model creation for table {table_name} on database {db_alias}")
        full_table_name = f"{schema_name}.{table_name}"
        try:
            dynamic_model = create_dynamic_model(full_table_name, db_alias)
            if dynamic_model:
                logger.debug(f"Model created: {dynamic_model.__name__}")
                print(f"Model created: {dynamic_model.__name__}")
        except Exception as e:
            logger.error(f"Error creating model for {full_table_name} in {db_alias}: {e}")
            print(f"Error creating model for {full_table_name} in {db_alias}: {e}")


def create_dynamic_model(table_name, db_alias):
    
    # Split schema and table name
    if '.' in table_name:
        schema_part, table_part = table_name.split('.', 1)
    else:
        schema_part = None
        table_part = table_name

    connection = connections[db_alias]

    with connection.cursor() as cursor:
        # if connection.connection:
        #     print(f"Database '{db_alias}' is connected.")
        # else:
        #     print(f"Database '{db_alias}' is NOT connected.")


        # Get columns
        if db_alias == 'oracle':
            cursor.execute(f'SELECT * FROM "{schema_part}"."{table_part}"')
            
        elif db_alias == 'postgresql':
            if schema_part:
                cursor.execute(f'SELECT * FROM "{schema_part}"."{table_part}"')  
            else:
                cursor.execute(f"SELECT * FROM '{table_part}'")

        else:
            cursor.execute(f"SELECT * FROM {table_part}")

        columns = [col[0] for col in cursor.description]

        # Detect primary key
        pk_columns = []
        if db_alias == 'oracle':
            cursor.execute(f"""
                SELECT cols.column_name
                FROM all_constraints cons, all_cons_columns cols
                WHERE cons.constraint_type = 'P'
                  AND cons.constraint_name = cols.constraint_name
                  AND cons.owner = UPPER('{schema_part}')
                  AND cols.table_name = UPPER('{table_part}')
            """)
            pk_columns = [row[0] for row in cursor.fetchall()]
        else:
            cursor.execute(f"""
                SELECT kcu.column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                  AND tc.table_schema = kcu.table_schema
                WHERE tc.table_schema = '{schema_part or 'public'}'
                  AND tc.table_name = '{table_part}'
                  AND tc.constraint_type = 'PRIMARY KEY'
            """)
            pk_columns = [row[0] for row in cursor.fetchall()]

        primary_key = pk_columns[0] if pk_columns else None

        print(f"Primary key: {primary_key}")
        logger.debug(f"Primary key: {primary_key}")

    # Prepare fields for the dynamic model
    fields = {
        '__module__': __name__,
        'Meta': type('Meta', (), {
            'managed': False,
            'db_table': f'"{schema_part}"."{table_part}"' if schema_part else f'"{table_part}"',
            'app_label': 'envA'
        }),
    }

    if primary_key == None and "id" in columns:
        primary_key = "id"

    for column in columns:
        if column == primary_key:
            fields[column] = models.IntegerField(primary_key=True)
        else:
            fields[column] = models.CharField(max_length=255)

    # Add some methods to get the model's details
    def get_fields(instance):
        return [{'name': f.name, 'value': getattr(instance, f.name)} for f in instance._meta.fields]

    def get_fields(cls):
        return [{'name': f.name, 'type': type(f).__name__, 'default': f.default if hasattr(f, 'default') else None} for f in cls._meta.fields]


    def list_methods(cls):
        return [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
    
    # Class methods to retrieve model's metadata
    def get_meta_options(cls):
        return {
            'db_table': cls._meta.db_table,
            'managed': cls._meta.managed,
            'app_label': cls._meta.app_label,
            'model_name': cls._meta.model_name,
            'verbose_name': cls._meta.verbose_name if hasattr(cls._meta, 'verbose_name') else cls._meta.model_name,
        }

    fields['get_fields'] = classmethod(get_fields)
    fields['get_meta_options'] = classmethod(get_meta_options)
    fields['list_methods'] = classmethod(list_methods)

    # Create dynamic model
    model_name = table_part.replace(' ', '_').replace('.', '_').capitalize()
    DynamicModel = type(model_name, (models.Model,), fields)

    # Register the dynamic model with the admin
    if DynamicModel:
        if not apps.is_installed('envA'):
            raise ImproperlyConfigured("The 'envA' app must be installed to use this functionality")
        print(DynamicModel.get_fields())
        logger.debug(DynamicModel.get_fields())
        print()
        print()
        register_dynamic_model(DynamicModel)

    #admin.site.register(DynamicModel)

    return DynamicModel