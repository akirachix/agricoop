from django.urls import path
from .views import home_page,add_group
from .views import profile

app_name= 'groups'

urlpatterns = [
    path("home/",home_page,name="home"),
    path("add/", add_group, name="add_group"),
    
  
]
