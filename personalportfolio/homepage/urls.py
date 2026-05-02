"""
URL configuration for the homepage app.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
]
