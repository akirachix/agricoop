from django.shortcuts import  render, redirect

from addgroup.models import Group_list
from .forms import GroupRegistrationForm
from .models import Delivaries
from  addgroup.models import Group_list
from django.http.response import HttpResponseRedirect
from django.urls import reverse

def group_details(request,id):
    groups=Group_list.objects.get(id = id)
    if request.method=="POST":
        form = GroupRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("group_details:list")
        else:
            print(form.errors)
    else:
        form= GroupRegistrationForm()
    return render(request,"group_details.html",{"form":form,"groups":groups})


def display_beans(request):
    products=Delivaries.objects.all()
    return render(request,"bean_details.html",{"products":products})

<<<<<<< HEAD
def grouped_bens(request,id):
    groups=Group_list.objects.get(id=id)
    return render(request,"group_details.html",{"groups":groups})


def profile(request,id):
    product=Delivaries.objects.get(id=id)
    return render(request,"profile.html",{"product":product})

=======
>>>>>>> 41b40fc7f92eec105a0b5d14755b91b20542487a
def edit(request,id):
    product=Delivaries.objects.get(id=id)
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("group_details:list")
    else:
        form=GroupRegistrationForm(instance=product)
        return render(request,"edit.html",{"form":form})

def delete(request,id):
    product=Delivaries.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return HttpResponseRedirect(reverse("group_details:list"))
    context={"product":product}
    return render(request,'delete.html')

