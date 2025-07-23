from django.urls import path
from .views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view(), name='api-note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view(), name='api-note-detail'),
]
