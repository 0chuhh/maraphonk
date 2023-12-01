from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages

import random

from .models import *
from .forms import *


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main')
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='ADMIN').exists():
                    return redirect("menu_admin")
                elif user.groups.filter(name='Runner').exists():
                    return redirect("menu_runner")
                elif user.groups.filter(name='Coordinator').exists():
                    return redirect("menu_coordinator")
            else:
                messages.error(request, 'Неверный логин или пароль!',
                               extra_tags='alert alert-danger alert-dismissible fade show'
                               )

    return render(request, "login.html", {"form": form})
