from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Tournaments
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('tournaments/add/', views.tournament_add, name='tournament_add'),
    path('tournaments/<int:pk>/edit/', views.tournament_edit, name='tournament_edit'),
    path('tournaments/<int:pk>/toggle/', views.tournament_toggle, name='tournament_toggle'),
    path('tournaments/<int:pk>/delete/', views.tournament_delete, name='tournament_delete'),

    # Gallery
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),
    path('gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:pk>/toggle/', views.gallery_toggle, name='gallery_toggle'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),

    # Team members
    path('team/', views.team_list, name='team_list'),
    path('team/add/', views.team_add, name='team_add'),
    path('team/<int:pk>/edit/', views.team_edit, name='team_edit'),
    path('team/<int:pk>/toggle/', views.team_toggle, name='team_toggle'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),

    # Contact messages
    path('messages/', views.contact_list, name='contact_list'),
    path('messages/<int:pk>/toggle-read/', views.contact_toggle_read, name='contact_toggle_read'),
    path('messages/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]
