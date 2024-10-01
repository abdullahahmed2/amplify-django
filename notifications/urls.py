# notifications/urls.py
from django.urls import path
from . import views
from notifications.views import send_notification


urlpatterns = [
    path('notify/', views.send_notification, name='send_notification'),
]
