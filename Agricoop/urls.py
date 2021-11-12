"""Agricoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registration.urls')),
    path('addgroup/',include('addgroup.urls')),
    path("group_details/",include("group_details.urls")),
    path("payments/",include("payments.urls")),
    path('settings/', include("settings.urls")),
    path('api/v1/', include('payments.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

