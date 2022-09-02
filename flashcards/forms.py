from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'name',
        )


# class DeckForm(forms.ModelForm):
#     class Meta:
#         model = Deck
#         fields = (
#             'Tennis',
#             'Music',
#         )