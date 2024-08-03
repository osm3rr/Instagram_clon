from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from publicaciones.models import tabla1


class HomePageView(ListView):

    model = tabla1
    template_name ="home.html"