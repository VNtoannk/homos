from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_ippub, name='ip_public'),
]