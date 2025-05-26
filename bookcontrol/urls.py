from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_books, name='register_books'),
]
