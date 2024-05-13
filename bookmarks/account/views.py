from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import loginForm

# Create your views here. 
def user_login(request):
    if request.method=='POST':
        form=loginForm(request.POST)
        if(form.is_valid()):
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password']
                              )
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("authenticated succesfuly")
                else:
                    return HttpResponse("your account is diabled right now ")
            else: 
               return HttpResponse("Invalid login")
    else: 
     form=loginForm()
    return render(request,'account/login.html',{'form':form})

