from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Flashcards(models.Model):
    pass


class Card(models.Model):
    pass


class Deck(models.Model):
    pass