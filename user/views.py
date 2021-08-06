from django.shortcuts import render,redirect
from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Registeration Success {username}')
            return redirect('/')
    else:
        form=RegisterForm()

    return render(request,'user/register.html',context={'form':form,'title':"Registeration"})


#christ47codedotcom