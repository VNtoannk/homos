from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('1/', views.taskdue, name='taskdue'),
]