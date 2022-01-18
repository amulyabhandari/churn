from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm,SignupForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
#def index (request):
  # return render (request,'churn/index.html')
class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'churn/index.html')
        form= LoginForm()
        context= {
            'form':form,
            }
        return render(request,'churn/index.html',context)
    def post(self,request):
        form= LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            branch = form.cleaned_data['branch']
            user= authenticate(username=username, password=password, branch=branch)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponse('user invalid')
#def index(request):
 #   return render(request, 'churn/index.html')
class RegsiterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'churn/index.html')
        form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, 'churn/signup.html',context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            branch = form.cleaned_data['branch']
            user = User(username=username, branch=branch, email=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        return HttpResponse('Forms not filled properly')
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


