from django import forms

from .models import Extruder, ProductSystem, Profile


class ExtruderForm(forms.ModelForm):
    class Meta:
        model = Extruder
        fields = ['extruder_name']
