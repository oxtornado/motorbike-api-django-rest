# motos_api/urls.py
from django.urls import path
from .views import MotoListApiView, MotoDetailApiView # Import the MotoListApiView class from views.py

urlpatterns = [
    path('', MotoListApiView.as_view(), name='moto-list'),
    path('<int:moto_id>', MotoDetailApiView.as_view(), name='moto-detail'),
]