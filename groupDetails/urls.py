from django.urls import path
from .views import groupDetails
urlpatterns = [
    path("",groupDetails,name="groupDetails")
]


