from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('cards'),
    # path('decks', views.decks_list, name='decks_list'),
    # path('', include('flashcards.urls')),
    # path('', views.flashcards, name='flashcards'),
    path('', views.index, name='index'),
]