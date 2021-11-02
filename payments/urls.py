from django.urls import path
from .views import payments,payment_list
from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path("payments/",payments,name="payments")
    path("payments/",payments,name="payments"),
    path("list/",payment_list,name="payment_list"),
]

