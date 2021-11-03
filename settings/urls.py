from django.urls import path
from .views import notifications, setting_page


urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
        path("",notifications,name="notifications"),
]
