from django import forms

from .models import Extruder, ProductSystem, Profile


class ExtruderForm(forms.ModelForm):
    class Meta:
        model = Extruder
        fields = ['extruder_name']


class ProductSystemForm(forms.ModelForm):
    class Meta:
        model = ProductSystem
        fields = ['system_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_code', 'profile_length', 'profile_weight']
