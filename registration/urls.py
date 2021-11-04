from django.urls import path
from . views import register_request ,logout_request,login_request,

urlpatterns = [
    path("",register_request,name="register"),
    path("login/", login_request, name="login"),
    path("logout/",logout_request, name= "logout"),
   
    
]