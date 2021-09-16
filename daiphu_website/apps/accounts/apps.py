from django.apps import AppConfig


AppConfig.default= False
class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    default = False
    
