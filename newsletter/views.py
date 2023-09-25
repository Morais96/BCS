from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SubscriberForm
from .models import Subscriber
from django.http import JsonResponse

def coming_soon_page(request):

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({'valid': True, 'subscribed': True})
        
        if form.is_valid():
            form.save()
            subject = 'Welcome to Burriqueira'
            message = 'Thank you for subscribing to our newsletter!'
            from_email = 'support@burriqueira.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({'valid': True, 'subscribed': False})
        else:
            return JsonResponse({'valid': False, 'subscribed': False})
    else:
        form = SubscriberForm()
        
    return render(request, 'comingsoon.html', {'form': form})