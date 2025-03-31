# motos_api/urls.py
from django.urls import path
from .views import MotoListApiVieww as MotoList # Import the MotoListApiView class from views.py

urlpatterns = [
    path('', MotoList.as_view(), name='moto-list'),  # URL pattern for the MotoListApiView
]