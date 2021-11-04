from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Delivaries

def group_details(request):
    if request.method=="POST":
        form = GroupRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group_details')
        else:
            print(form.errors)
    else:
        form= GroupRegistrationForm()
    return render(request,"group_details.html",{"form":form})

def display_beans(request):
    products=Delivaries.objects.all()
    return render(request,"bean_details.html",{"products":products})

def profile(request,id):
    product=Delivaries.objects.get(id=id)
    return render(request,"profile.html",{"product":product})

def edit(request,id):
    product=Delivaries.objects.get(id=id)
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect(display_beans)  
    else:
        form=GroupRegistrationForm(instance=product) 
    return render(request,"edit.html",{"form":form})        

