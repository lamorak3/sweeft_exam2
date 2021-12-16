from django import forms

from .models import Short_Data

class Url(forms.Form):
    #klasi Url gamoiyeneba views.py-shi
    url = forms.URLField(label="URL")