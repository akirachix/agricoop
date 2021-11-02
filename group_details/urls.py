from django.urls import path
from .views import delete, group_details,display_beans,edit,profile

urlpatterns = [
        path("",group_details,name="group_details"),
        path("group_details/",display_beans,name="list"),
        path("profile/<int:id>/",profile,name="profile"),
        path("edit/<int:id>/",edit,name="edit"),
        path("delete/<int:id>/",delete,name="delete")
        
]