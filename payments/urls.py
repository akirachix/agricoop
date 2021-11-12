from django.urls import path
from .views import payments,payment_list,edit,delete
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .import views

app_name = 'payments'
urlpatterns = [
    path("payments/",payments,name="payments"),
    path("list/",payment_list,name="payment_list"),
    path("edit/<int:id>/",edit,name="edit"),
    path("delete/<int:id>/",delete,name="delete"),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),

]
