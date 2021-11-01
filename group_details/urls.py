from django.urls import path
from .views import group_details,display_beans,edit,profile
# app_name='group_details'
urlpatterns = [
        path("",group_details,name="group_details"),
        path("group_details/",display_beans,name="list"),
        path("profile/<int:id>/",profile,name="profile"),
        path("edit/<int:id>/",edit,name="edit")
        
]