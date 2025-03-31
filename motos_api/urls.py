# motos_api/urls.py
from django.urls import path
from .views import MotoListApiView # Import the MotoListApiView class from views.py

urlpatterns = [
    path('', MotoListApiView.as_view(), name='moto-list'),
]