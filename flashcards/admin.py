from django.contrib import admin
from .models import Card, Deck, User


admin.site.register(User)
admin.site.register(Card)
admin.site.register(Deck)#

# admin.site.register