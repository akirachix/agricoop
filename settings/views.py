from django.shortcuts import redirect, render

# Create your views here.
def account(request):
    return redirect(request,template_name='account.html')