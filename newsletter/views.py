from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from .forms import SubscriberForm
from .models import Subscriber
from django.http import JsonResponse
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.conf import settings
import os

def logo_data(image):
    path = os.path.join(settings.MEDIA_ROOT, image)
    with open(path, 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    return logo

def coming_soon_page(request):

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({'valid': True, 'subscribed': True})
        
        if form.is_valid():
            form.save()
            
            message = EmailMultiAlternatives(
                subject='Welcome to Burriqueira',
                body=render_to_string('welcome_email.html', {}).strip(),
                from_email='support@burriqueira.com',
                to=[email]
            )
            message.content_subtype = 'html'
            message.mixed_subtype = 'related'
            message.attach(logo_data('00011.jpeg'))
            message.attach(logo_data('00009.jpeg'))

            message.send(fail_silently=False)

            return JsonResponse({'valid': True, 'subscribed': False})
        else:
            return JsonResponse({'valid': False, 'subscribed': False})
    else:
        form = SubscriberForm()
        
    return render(request, 'comingsoon.html', {'form': form})