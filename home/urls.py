from django.urls import path
from .views import home_page,add_group

app_name = 'Home'
urlpatterns = [
    path("home/",home_page,name="home"),
    path("add_group/",add_group,name="add_group")
]
    
