from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def start(self):
        import users.signals