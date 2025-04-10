from django.shortcuts import render
from django.views.generic import TemplateView 

class HomeView(TemplateView):
    # model = Model
    template_name = "home.html"
