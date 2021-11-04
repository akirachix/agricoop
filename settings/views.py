from django.shortcuts import render
from .models import Setting_page, privacy_info
from.forms import SettingRegistrationForm


def setting_page(request):
    form= SettingRegistrationForm()
    return render(request,"setting_page.html",{form:"form"})

def privacy_page(request):
    return render(request,"privacy_page.html")