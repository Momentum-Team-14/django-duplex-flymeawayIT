from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('cards', views.cards, name='cards'),
    path('decks', views.decks_list, name='decks_list'),
    path('', include('flashcards.urls')),
    path('', views.flashcards, name='flashcards'),
]