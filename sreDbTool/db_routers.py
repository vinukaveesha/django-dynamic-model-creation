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

class MultiDBRouter:
    def db_for_read(self, model, **hints):
        """Directs reads to PostgreSQL by default unless specified."""
        if model._meta.app_label == 'envA':
            return 'oracle'  
        return None

    def db_for_write(self, model, **hints):
        """Directs writes to PostgreSQL by default unless specified."""
        if model._meta.app_label == 'envA':
            return 'oracle'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both models use the same DB."""
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'envA':
            return db == 'oracle'
        return db == 'default'

