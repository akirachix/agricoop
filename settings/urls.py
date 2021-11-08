from django.urls import path
from .views import accounts, setting_page,delete,user_name

from .views import help ,setting_page

from .views import notifications, setting_page

appname='settings'

urlpatterns = [
        path("settings/",setting_page,name="settings_page"),
        path("accounts/",accounts,name="accounts"),
        # path("delete/",delete,name="delete"),
        # path('profile/', user_views.profile, name='profile'),
        path('del-user/<slug:username>', delete, name='delete'),
        path('user_name/<slug:username>', user_name, name='user'),

        path("help/",help,name="help"),

        path("",notifications,name="notifications"),
]
