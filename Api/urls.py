from django.urls.conf import include, path
from rest_framework import routers
from .views import LoginViewSet
from .views import SignUpViewSet
from .views import PaymentViewSet
from .views import BaseModelViewset
from .views import MpesaCallsViewset
from .views import MpesaCallBacksViewset
from .views import MpesaPaymentViewset
router=routers.DefaultRouter()
router.register("login/",LoginViewSet)
router.register("register/",SignUpViewSet)
router.register("dashboard/",PaymentViewSet)
router.register("basemodel/",BaseModelViewset)
router.register("mpesacalls/",MpesaCallsViewset)
router.register("mpesacallbacks/",MpesaCallBacksViewset)
router.register("mpesapayment/",MpesaPaymentViewset)
urlpatterns = [
   path("",include(router.urls))
]