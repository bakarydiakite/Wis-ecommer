from django import forms
from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre adresse email',
            'autocomplete': 'email',
        }),
        label="Recuperation"  # Remplace "Courrier" par "Email"
    )