from django.shortcuts import render
# from .models import flashcards


def index(request):
    return render(request, 'index.html', {})


# def card_add(request):
#     cards = cards.objects.all()
#     return render(request, 'flashcards/card_add.html', {}) 


# def cards_list(request):
#     flashcards = flashcards.objects.all()
#     return render(request, 'flashcards/cards_list.html', {"flashcards:flashcards"})


# def flash_cards(request):
#     return render(request, 'flashcards/flash_cards.html', {'flashcards':flashcards})