from django.shortcuts import render
from .models import Flashcards, Index, Card


def index(request):
    index = Index.objects.all()
    return render(request, 'index.html', {'index': index})


# def card_add(request):
#     cards = Card.objects.all()
#     return render(request, 'flashcards/card_add.html', {'flashcards': flashcards}) 


# def cards_list(request):
#     flashcards = Flashcards.objects.all()
#     return render(request, 'flashcards/cards_list.html', {'flashcards':flashcards})


# def flash_cards(request):
#     flashcards = Flashcards.objects.all()
#     return render(request, 'flashcards/flash_cards.html', {'flashcards':flashcards})