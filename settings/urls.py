from django.urls import path
from .views import help ,setting_page


urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
        path("help/",help,name="help"),
]
