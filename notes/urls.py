from django.urls import path
from .views import (
    RegisterView,
    NotesView,
    UpdateNoteView,
    DeleteNoteView
)

urlpatterns = [

    # Register
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    # Get all notes + Create note
    path(
        "notes/",
        NotesView.as_view(),
        name="notes"
    ),

    # Update note
    path(
        "notes/update/<int:id>/",
        UpdateNoteView.as_view(),
        name="update-note"
    ),

    # Delete note
    path(
        "notes/delete/<int:id>/",
        DeleteNoteView.as_view(),
        name="delete-note"
    ),
]