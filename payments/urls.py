from django.urls import path
from .views import payments,payment_list,edit,delete,lipa
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'payments'
urlpatterns = [
    path("payments/",payments,name="payments"),
    path("list/",payment_list,name="payment_list"),
    path("edit/<int:id>/",edit,name="edit"),
    path("delete/<int:id>/",delete,name="delete"),
    path("lipa",lipa,name="lipa"),
    

]
