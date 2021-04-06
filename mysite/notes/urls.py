from django.contrib import admin
from django.urls import path

from notes.views import editor, delete_document

urlpatterns = [
    path('notes/', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
]
