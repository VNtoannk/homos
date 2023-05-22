from django import forms
from .models import Site, IP_public_test


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

class IP_public_test_Form(forms.ModelForm):
    class Meta:
        model = IP_public_test
        fields = '__all__'