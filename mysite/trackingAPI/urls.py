from django.urls import path

from .views import ListCryptocurrencyView

urlpatterns = [
    path('', ListCryptocurrencyView.as_view(), name='listcc'),
    
]
