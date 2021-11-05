from django.urls import path
from .views import add_group,display_group


app_name = 'addgroup'
urlpatterns = [
    path("add_group/",add_group,name="add_group"),
    path("display/", display_group, name="display_group"),
]
    
