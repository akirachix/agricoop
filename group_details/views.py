from django.shortcuts import  render, redirect
from .forms import GroupRegistrationForm
from .models import Group_details

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

    
def profile(request,id):
    product=Group_details.objects.get(id=id)
    return render(request,"profile.html",{"product":product})


def profile(request,id):
    product=Group_details.objects.get(id=id)
    return render(request,"profile.html",{"product":product})

def edit(request,id):
    product=Group_details.objects.get(id=id)
    if request.method=="POST":
        form=GroupRegistrationForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect(display_beans)
    else:
        form=GroupRegistrationForm(instance=product)
        return render(request,"edit.html",{"form":form})
        
         

