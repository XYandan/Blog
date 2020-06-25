from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm

# Create your views here.
#登录 注册页面
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #内置表单

        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')

    else:
        form = SignUpForm()

    return render(request,'signup.html',{'form':form})
