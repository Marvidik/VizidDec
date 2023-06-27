from django import forms 
from django.forms import TextInput, Textarea,EmailInput
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'input-control', 'id': 'name', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'input-control', 'id': 'email','placeholder':'Email'}),
            'subject': TextInput(attrs={'class': 'input-control', 'id': 'subject', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input-control', 'id': 'messageon',
                                                'placeholder': 'Write Your Message','rows':10}),
            
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'class': 'input-control', 'id': 'email','placeholder':'Email'}),
        }