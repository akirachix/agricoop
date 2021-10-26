from django.urls import path
from . views import register_request ,logout_request,login_request,index

urlpatterns = [
    path("",index,name="home"),
    path("register/",register_request,name="register"),
    path("login/", login_request, name="login"),
    path("logout/",logout_request, name= "logout"),
   
    
]