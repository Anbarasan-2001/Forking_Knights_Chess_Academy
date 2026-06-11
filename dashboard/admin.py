from django.contrib import admin
from .models import Tournament, GalleryImage, TeamMember, ContactMessage


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'game_format', 'start_date', 'end_date', 'status', 'is_active')
    list_filter = ('status', 'game_format', 'is_active')
    search_fields = ('name', 'location')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'tournament', 'category', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'tournament')
    search_fields = ('title',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'jersey_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'role')
    search_fields = ('name', 'role')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'message')
