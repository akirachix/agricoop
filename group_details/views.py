from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Group_details
from django.http.response import HttpResponseRedirect
from django.urls import reverse

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
    products=Group_details.objects.all()
    return render(request,"bean_details.html",{"products":products})

def edit(request,id):
    product=Group_details.objects.get(id=id)
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("group_details:list")
    else:
        form=GroupRegistrationForm(instance=product)
        return render(request,"edit.html",{"form":form})

def delete(request,id):
    product=Group_details.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return HttpResponseRedirect(reverse("group_details:list"))
    context={"product":product}
    return render(request,'delete.html')        
        
         

