from django.urls import path
from .views import group_details
urlpatterns = [
    path("",group_details,name="group_details")
]


