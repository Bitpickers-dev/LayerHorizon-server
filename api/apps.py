from django.apps import AppConfig
from api.scheduler import auto_chache_blocks


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        auto_chache_blocks()
