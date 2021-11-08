from django.shortcuts import render
from .models import Setting_page
from.forms import SettingRegistrationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls import reverse

def setting_page(request):
    form= SettingRegistrationForm()
    return render(request,"setting_page.html",{form:"form"})

def accounts(request):
    profile=Setting_page.objects.all()
    return render(request,"account.html",{"profile":profile})

# def image(request):
#     user = User.objects.get(username='<admin_user_name>')
#     profiles = avatar(user=user)
#     profiles.save()
#     return render(request,"account.html")

def user_name(request,newusername):
    if User.objects.filter(username=newusername).exists():
        raise SettingRegistrationForm.ValidationError(u'Username "%s" is not available.' % newusername)
    user = User.objects.get(username = user_name)
    user.username = newusername
    user.save()
    return render(request,"account.html")  

def delete(request, username):
    context = {}
    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = 'The user is deleted.' 
        return HttpResponseRedirect(reverse("delete"))
    except User.DoesNotExist: 
        context['msg'] = 'User does not exist.'
    except Exception as e: 
        context['msg'] = e.message
    return render(request, 'registration:register.html', context=context)     
