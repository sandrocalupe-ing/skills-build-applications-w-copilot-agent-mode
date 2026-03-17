"""Views for the OctoFit Tracker API."""

from rest_framework import viewsets

from .models import Activity, Team, UserProfile
from .serializers import ActivitySerializer, TeamSerializer, UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


    class WorkoutViewSet(viewsets.ModelViewSet):
        queryset = Workout.objects.all().order_by('name')
        serializer_class = WorkoutSerializer


        class LeaderboardEntryViewSet(viewsets.ModelViewSet):
            queryset = LeaderboardEntry.objects.all().order_by('rank')
            serializer_class = LeaderboardEntrySerializer
