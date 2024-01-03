from typing import Any
from .models import Room
from django import forms


class RoomForm(forms.ModelForm):
    fields = []

    class Meta:
        model = Room
        exclude = ['hotel']
