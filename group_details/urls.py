from django.urls import path
from .views import products

urlpatterns = [
    path("group_details/",products,name="products")
]

