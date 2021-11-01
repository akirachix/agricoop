from django.urls import path
# from .views import payments
from .views import payment_list, payments

app_name = 'payments'
urlpatterns = [
    # path("payments/",payments,name="payments")
    path("payments/",payments,name="payments"),
    path("list/",payment_list,name="payment_list"),
]