from django import forms
from django.forms import fields
from .models import  buy_details

class BuyForm(forms.ModelForm):
    class Meta:
        model = buy_details
        fields = "__all__"