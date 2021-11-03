from django .urls.conf import path

from .views import account

urlpatterns=[
    path("settings/",account,name=account)

]

