from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Enter your email'
    }))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Write your message here', 
        'rows': 4
    }))