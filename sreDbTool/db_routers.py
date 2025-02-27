# class MultiDBRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'envA':  # Assuming models are within 'envA' app
#             return 'oracle' if 'oracle' in model._meta.db_table else 'default'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'envA':
#             return 'oracle' if 'oracle' in model._meta.db_table else 'default'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         db1 = obj1._state.db
#         db2 = obj2._state.db
#         if db1 and db2:
#             return db1 == db2
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'envA':
#             return False  # Prevent migrations for dynamic models
#         return None

# class MultiDBRouter:
#     def db_for_read(self, model, **hints):
#         """Directs reads to PostgreSQL by default unless specified."""
#         if model._meta.app_label == 'envA':
#             return 'oracle'  
#         return None

#     def db_for_write(self, model, **hints):
#         """Directs writes to PostgreSQL by default unless specified."""
#         if model._meta.app_label == 'envA':
#             return 'oracle'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """Allow relations if both models use the same DB."""
#         return obj1._state.db == obj2._state.db

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'envA':
#             return db == 'oracle'
#         return db == 'default'


# class MultiDBRouter:
#     """
#     A router to control all database operations on models in the 'envA' application.
#     """
#     ROUTE_APP_LABELS = {'envA'}

#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read envA models go to their associated database.
#         """
#         if model._meta.app_label in self.ROUTE_APP_LABELS:
#             return model._meta.db_table.split('.')[0]
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write envA models go to their associated database.
#         """
#         return self.db_for_read(model, **hints)

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the envA app is involved.
#         """
#         if obj1._meta.app_label in self.ROUTE_APP_LABELS or \
#            obj2._meta.app_label in self.ROUTE_APP_LABELS:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the envA app only appears in the 'oracle' database.
#         """
#         if app_label in self.ROUTE_APP_LABELS:
#             return db == 'oracle'
#         return None

class MultiDBRouter:
    """
    A router to control database operations for non-admin models.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'envA':
            return 'oracle' if 'oracle' in model._meta.db_table else 'postgresql'
        return 'default'

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'envA' :
            return db in ['postgresql', 'oracle']
        return db == 'default'


