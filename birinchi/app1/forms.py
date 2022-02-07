from django import forms
from .models import Kitob,Muallif



class KitobForm(forms.ModelForm):
    class Meta:
        model= Kitob
        fields=['nom','sahifa','tur']
class MuallifForm(forms.ModelForm):
    class Meta:
        model=Muallif
        fields=['ism','yosh','jinsi']


