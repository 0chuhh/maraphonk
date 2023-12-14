from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main_page/main.html'


class BMI(TemplateView):
    template_name = 'bmi/bmi.html'


class BMR(TemplateView):
    template_name = 'bmr/bmr.html'