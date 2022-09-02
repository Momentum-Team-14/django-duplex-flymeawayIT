from django.urls import reverse_lazy 
from django.views.generic import (ListView, CreateView, UpdateView)
from .models import Card

# from django.shortcuts import render


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('card-create')


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy('card-list')

# def flash_cards(request):
#     flashcards = Flashcard.objects.all()
#     return render(request, 'flashcards/flash_cards.html', {'flashcards':flashcards})


# def card_add(request):
#     cards = Card.objects.all()
#     return render(request, 'flashcards/card_add.html', {'flashcards': flashcards}) 


# def cards_list(request):
#     flashcards = Flashcards.objects.all()
#     return render(request, 'flashcards/cards_list.html', {'flashcards':flashcards})
