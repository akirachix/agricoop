from django.urls import path
# from .views import payments
from .views import payments
urlpatterns = [
    # path("payments/",payments,name="payments")
    path("payments/",payments,name="payments")
]