from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import notes

class HomeView(CreateView):

    model = notes
    template_name = 'home.html'
    fields = '__all__'