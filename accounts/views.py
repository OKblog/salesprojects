from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as BaseLoginView

# Create your views here.
from .forms import SignUpForm, LoginForm 

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('sales')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        account_id = form.cleaned_data.get('account_id')
        password = form.cleaned_data.get('password1')
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response
    
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'