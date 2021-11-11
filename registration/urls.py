from django.urls import path
from . views import register_request ,logout_request,login_request

urlpatterns = [
    path("", login_request, name="login"),
    path("reister",register_request,name="register"),
    path("logout/",logout_request, name= "logout"),

]