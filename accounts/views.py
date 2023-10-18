from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.shortcuts import render



def login_view(request):
    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
        
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form':form})


def terms_view(request):
    return render(request,'account/terms.html')



