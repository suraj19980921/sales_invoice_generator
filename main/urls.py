from django.urls import path
from main import views


urlpatterns = [
    path('', views.GenerateInvoice.as_view(), name='generate_invoice'),
]