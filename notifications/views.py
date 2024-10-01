from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def send_notification(request):
    # Extract the message from the request
    message = request.data.get('message', 'No message provided')
    
    # Recipient email and subject (you can extract these from the request or set them statically)
    recipient_email = request.data.get('recipient_email', 'recipient@example.com')
    subject = request.data.get('subject', 'Notification')

    # Sending the email using Django's send_mail function
    try:
        send_mail(
            subject,  # Subject of the email
            message,  # Body of the email
            'your_email@example.com',  # Sender's email (configured in settings.py)
            [recipient_email],  # List of recipient emails
            fail_silently=False,  # If True, suppresses any errors
        )
        return Response({'status': 'Notification sent'}, status=200)

    except Exception as e:
        # If there's any error during the email sending, return a failure response
        return Response({'status': 'Failed to send notification', 'error': str(e)}, status=500)
