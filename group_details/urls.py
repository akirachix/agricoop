from django.urls import path

from .views import group_details,display_beans,edit,delete,grouped_bens

app_name = 'group_details'
urlpatterns = [
        path("group_details/",group_details,name="group_details"),
        path("group_details/<int:id>/",grouped_bens,name="group_details"),
        path("group_details/",display_beans,name="list"),
        path("edit/<int:id>/",edit,name="edit"),
        path("delete/<int:id>/",delete,name="delete")


]
