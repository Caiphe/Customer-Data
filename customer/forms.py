from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    birth_date = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Date of Birth','type': 'date'}))

    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'birth_date', 'file']
    
      