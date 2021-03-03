from django import forms
from .models import TodoModel, Post

class FloorForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"


