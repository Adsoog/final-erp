from django import forms
from apps.partners.models.partner import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
