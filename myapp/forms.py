from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo # connection of model to form
        fields = ['title', 'description', 'content', 'image', 'video']