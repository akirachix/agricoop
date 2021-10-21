from django.urls import path
from .views import login_request, logout_request

  


urlpatterns = [
    path("login/", login_request, name="login"),
    path("logout/",logout_request, name= "logout"),
]