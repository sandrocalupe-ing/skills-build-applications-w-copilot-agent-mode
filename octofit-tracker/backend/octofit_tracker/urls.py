"""octofit_tracker URL Configuration.

The `urlpatterns` list routes URLs to views.

This project exposes a small API surface. It is designed to work both locally
and when running in a GitHub Codespace (using the CODESPACE_NAME environment var).
"""

import os

from django.contrib import admin
from django.urls import include, path

from .api import api_root, router

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
