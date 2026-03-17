"""API wiring for the OctoFit Tracker backend.

This module provides a small DRF router and a root endpoint for basic API discovery.
"""

from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .views import ActivityViewSet, TeamViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='userprofile')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'teams', TeamViewSet, basename='team')


@api_view(['GET'])
def api_root(request, format=None):
    """A small root endpoint that can be hit with curl for quick sanity checking."""

    return Response(
        {
            'status': 'ok',
            'api_base': request.build_absolute_uri('/api/'),
            'message': 'Welcome to OctoFit Tracker API',
        }
    )
