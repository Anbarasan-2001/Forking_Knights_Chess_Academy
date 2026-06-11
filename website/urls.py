from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('contact/', views.contact, name='contact'),
    path('team_details/', views.team_details, name='team_details'),
    path('team_details/<int:pk>/', views.team_details, name='team_details'),
]