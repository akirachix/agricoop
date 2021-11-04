from django.shortcuts import redirect,render
from .models import Setting_page
from.forms import SettingRegistrationForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.conf import settings


def setting_page(request):
    form= SettingRegistrationForm()
    return render(request,"setting_page.html",{form:"form"})



@require_GET
def notifications(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'notifications.html', {user: user, 'vapid_key': vapid_key})
