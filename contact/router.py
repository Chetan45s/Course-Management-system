class CheckerRouter:
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'contact':
            return 'contactdb'
        if model._meta.app_label == 'validate':
            return 'validatedb'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'contact':
            return 'contactdb'
        if model._meta.app_label == 'validate':
            return 'validatedb'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'contact' or obj2._meta.app_label == 'contact':
            return True
        elif 'contact' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'contact':
            return db == 'contactdb'
        if app_label == 'validate':
            return db == 'validatedb'


