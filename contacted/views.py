from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validation (optional)
        if not name or not email or not message:
            messages.error(request, 'All fields are required.')
        else:
            # Send email
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],  # Your email
            )
            messages.success(request, 'Your message has been sent successfully!')
            return HttpResponseRedirect('/contact/')  # Reload to clear the form

    return render(request, 'contact.html')

    