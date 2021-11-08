from django.urls import path
from .views import accounts, setting_page,delete,user_name

appname='settings'

urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
        path("accounts/",accounts,name="accounts"),
        # path("delete/",delete,name="delete"),
        # path('profile/', user_views.profile, name='profile'),
        path('del-user/<slug:username>', delete, name='delete'),
        path('user_name/<slug:username>', user_name, name='user'),
]
