from django.db import models

# Create your models here.
# notifications/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def send_notification(request):
    message = request.data.get('message', 'No message provided')
    # You can use an email or messaging system here for real notifications
    print(f'Notification sent: {message}')
    return Response({'status': 'Notification sent'}, status=200)
