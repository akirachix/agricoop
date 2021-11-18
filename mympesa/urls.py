from django.urls import path, include
from . views import index,stk_push_callback,stk_timeout,result_url

app_name="mympesa"
urlpatterns = [
    path('index/',index, name='index'),
    path('daraja/stk-push/',stk_push_callback, name='mpesa_stk_push_callback'),
    path('stk+timeout/',stk_timeout, name='timeout'),
    path('result_url/',result_url, name='result'),
]