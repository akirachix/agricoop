from django.urls import path

from .views import help ,setting_page

from .views import notifications, setting_page
6


urlpatterns = [
        path("settings/",setting_page,name="settings_page"),

        path("help/",help,name="help"),

        path("",notifications,name="notifications"),
]
