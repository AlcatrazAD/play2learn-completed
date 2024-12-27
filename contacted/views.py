from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

class ContactThankView(TemplateView):
    template_name = 'contact/thanks.html'
   
