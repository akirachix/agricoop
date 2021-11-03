from django.shortcuts import redirect,render
from .models import Setting_page
from.forms import SettingRegistrationForm


def setting_page(request):
    form= SettingRegistrationForm()
    return render(request,"setting_page.html",{form:"form"})


def notifications(request):
    if request.method=="POST":
        form = SettingRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notifications')
        else:
            print(form.errors)
    else:
        form= SettingRegistrationForm()
        return render(request,"notifications.html",{"form":form})
