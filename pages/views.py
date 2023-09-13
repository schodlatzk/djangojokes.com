from django.shortcuts import render
from drjango.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"
