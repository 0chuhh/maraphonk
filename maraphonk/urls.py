"""
URL configuration for maraphonk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marathon.views import MainView, BMI, BMR, MarathonAboutPage, RunnerMenuPage


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', MainView.as_view(), name='main'),
    path('about/', MarathonAboutPage.as_view(), name='about'),
    path('bmi/', BMI.as_view(), name='bmi'),
    path('bmr/', BMR.as_view(), name='bmr'),
    path('runner-menu/', RunnerMenuPage.as_view(), name='runner_menu'),
    path('accounts/', include('accounts.urls')),
]
