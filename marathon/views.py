from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Marathon

class MainView(TemplateView):
    template_name = 'main_page/main.html'


class BMI(TemplateView):
    template_name = 'bmi/bmi.html'


class BMR(TemplateView):
    template_name = 'bmr/bmr.html'


class MarathonAboutPage(TemplateView):
    template_name = "about/about.html"
    extra_context = {'marathon': Marathon.objects.get(name="Huge keep similar it pressure bring.")}