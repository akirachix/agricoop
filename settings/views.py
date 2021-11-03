from django.shortcuts import render
from .models import Setting_page
from.forms import SettingRegistrationForm


def setting_page(request):
    form= SettingRegistrationForm()
    return render(request,"setting_page.html",{form:"form"})
