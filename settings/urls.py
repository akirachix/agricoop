from django.urls import path
from .views import setting_page, privacy_page


urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
        path("privacy/",privacy_page,name="privacy"),

]
