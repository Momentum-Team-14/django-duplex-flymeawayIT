from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import flashcards.Users


class Base(models.Model):
    pass


class Index(models.Model):
    pass


class User(AbstractUser):
    pass 
    # class Meta:
    #     db_table = 'auth_user'


class Flashcard(models.Model):
    pass


class Deck(models.Model):
    pass