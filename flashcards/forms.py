from django import forms
from .models import Decks, Cards, Deck, Card


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = (
            'Tennis',
            'Music',
        )


class CardForm(forms.ModelForm):
    class Meta:
        model = Card 
        fields = (
            'name',
        )
