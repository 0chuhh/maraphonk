from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from django.views.generic import CreateView
from .forms import CommonUserCreationForm
import random
from django.contrib.auth.models import Group

from .models import *
from .forms import *


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class SignUp(CreateView):
    model = User
    form_class = CommonUserCreationForm
    template_name = "registration/registration.html"
    # success_url = reverse_lazy("root:main")

    def post(self, request, *args, **kwargs):
        form = CommonUserCreationForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                middle_name=form.cleaned_data.get('middle_name'),
                last_name=form.cleaned_data.get('last_name'),
                image=form.cleaned_data.get('photo'),
                country=form.cleaned_data.get('country'),
            )
            user.set_password(form.cleaned_data.get('password1'))
            print(form.cleaned_data.get('role'))
            group = Group.objects.get(name=form.cleaned_data.get('role'))
            print(group)
            print(user)
            user.save()
            user = User.objects.get(email=form.cleaned_data.get('email'))
            user.groups.add(group)
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('main')

        return redirect('main')
