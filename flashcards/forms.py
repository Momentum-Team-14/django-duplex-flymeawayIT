# from django import forms
from .models import Card


# class CardCheckForm(forms.Form):
#     card_id = forms.IntegerField(required=True)
#     solved = forms.BooleanField(required=False)


# class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = (
            'name',
        )
