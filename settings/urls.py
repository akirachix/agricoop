from django.urls import path
from .views import setting_page


urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
]
