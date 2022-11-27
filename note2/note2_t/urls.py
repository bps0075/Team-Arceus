from django.urls import path
from .views import HomeView, NotesView, UpdateNotesView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('notes', NotesView.as_view(), name = 'notes'),
    path('notes/edit/<int:pk>',UpdateNotesView.as_view(),name='update_notes')
]
