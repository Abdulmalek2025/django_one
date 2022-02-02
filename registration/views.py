from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegisterUserForm

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = RegisterUserForm
    success_url = '/accounts/login/'