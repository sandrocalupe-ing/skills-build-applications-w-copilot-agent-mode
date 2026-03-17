"""Admin registration for the OctoFit Tracker models."""

from django.contrib import admin

from .models import Activity, Team, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'display_name', 'created_at')
    search_fields = ('username', 'email', 'display_name')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'duration_minutes', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'notes', 'user__username')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
