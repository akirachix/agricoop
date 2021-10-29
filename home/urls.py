from django.urls import path
from .views import home_page
from .views import profile

urlpatterns = [
    path("home/",home_page,name="home"),
    path('profile/', profile, name='users-profile'),
]

