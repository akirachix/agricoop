from django.urls import path
from .views import help ,setting_page
from .views import notifications, setting_page, privacy_page

from .views import accounts, setting_page,delete,user_name

urlpatterns = [
        path("settings/",setting_page,name="setting_page"),
        path("help/",help,name="help"),
        path("",notifications,name="notifications"),
        path('del-user/<slug:username>', delete, name='delete'),
        path('user_name/<slug:username>', user_name, name='user'),
        path("help/",help,name="help"),
        path("accounts/",accounts,name="accounts"),
        path("privacy/",privacy_page,name="privacy"),

]