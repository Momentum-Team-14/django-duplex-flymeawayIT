from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import flashcards.Users


class User(AbstractUser):
    pass 
    # class Meta:
    #     db_table = 'auth_user'


class Flashcards(models.Model):
    pass


class Card(models.Model):
    pass


class Deck(models.Model):
    pass