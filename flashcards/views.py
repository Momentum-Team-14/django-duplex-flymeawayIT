from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
# from django.views.generic import CardListView
from .models import Card
import random
# from django.shortcuts import get_object_or_404, redirect
# from .forms import CardCheckForm
from django.shortcuts import render


# changed CardListView from RP tutorial in Line 9 to ListView to resolve CardListView undefined
class BoxView(ListView):
    template_name = 'flashcards/box.html'
    # form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs['box_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
    #         card.move(form.cleaned_data["solved"])

    #     return redirect(request.META.get("HTTP_REFERER"))


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('box', '-date_created')


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
