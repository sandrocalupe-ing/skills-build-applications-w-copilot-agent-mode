"""Mongo-backed data models for the OctoFit Tracker app."""

from django.utils import timezone
from djongo import models


class UserProfile(models.Model):
    """A user profile for a fitness tracker user."""

    id = models.ObjectIdField(primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True, null=True)
    display_name = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Activity(models.Model):
    """A tracked activity performed by a user."""

    id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.duration_minutes}m)"


class Team(models.Model):
    """A simple team for grouping users."""

    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, unique=True)
    member_ids = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
