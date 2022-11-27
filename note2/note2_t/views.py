from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import notes

class HomeView(ListView):

    model = notes
    template_name = 'home.html'

class NotesView(CreateView):

    model = notes
    template_name = 'notes.html'
    fields = '__all__'

class UpdateNotesView(UpdateView):
    model = notes
    template_name = 'update_notes.html'
    fields = ['title', 'body']
