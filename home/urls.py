from django.urls import path
from .views import home_page,add_group, edit, delete

app_name= 'groups'

urlpatterns = [
    path("home/",home_page,name="home_group"),
    path("add/",add_group,name="add_group"),
    path("edit/<int:id>/",edit,name="edit"),
    path("delete/<int:id>/",delete,name="delete")

]