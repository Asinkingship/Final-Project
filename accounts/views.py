from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UserSignupForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('home')
    
class UserSignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserSignupForm

    def get_success_url(self):
        return reverse('login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        pass_text = form.cleaned_data['password']
        user.set_password(pass_text)

        user.save()
        return super().form_valid(form)

def log_user_out(request):
    logout(request)
    return redirect('login')
