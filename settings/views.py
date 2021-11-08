from django.shortcuts import redirect,render
from .models import Setting_page
from.forms import SettingRegistrationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponse
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings


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

def help(request):
    return render(request,"help.html")

@require_GET
def notifications(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'notifications.html', {user: user, 'vapid_key': vapid_key})

def privacy_page(request):
    return render(request,"privacy_page.html")