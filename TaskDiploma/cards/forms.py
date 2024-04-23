from django import forms
from cards.models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'task', 'performer']


class CardEditForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'task', 'performer']