from django.urls import path
from .views import HomeView, NotesView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('notes', NotesView.as_view(), name = 'notes'),

]
