from django.urls import path
from .views import login_request, logout_request
from .views import home_page

  


urlpatterns = [
    path("login/", login_request, name="login"),
    path("logout/",logout_request, name= "logout"),
    path("homepage",home_page,name="homepage"),

]