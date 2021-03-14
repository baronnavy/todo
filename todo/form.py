from django import forms
from .models import TodoModel, Post,Reservation

class FloorForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"


