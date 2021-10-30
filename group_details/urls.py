from django.urls import path
from django.conf.urls import url
from .views import group_details
urlpatterns = [
    path("",group_details,name="group_details")
]


