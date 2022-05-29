from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('profiles:succes_signup')
    template_name = 'profiles/signup.html'

class SuccesLoginPage(TemplateView):
    template_name = 'profiles/succes_login.html'

class SuccesLogoutPage(TemplateView):
    template_name = 'profiles/succes_logout.html'

class SuccesSignupPage(TemplateView):
    template_name = 'profiles/succes_signup.html'
