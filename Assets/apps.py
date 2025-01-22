from django.apps import AppConfig
import os

class AssetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Assets'
    path = os.path.join(os.path.dirname(__file__))
