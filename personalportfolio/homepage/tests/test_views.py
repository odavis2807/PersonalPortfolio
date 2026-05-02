"""
Tests for the homepage views.
"""

import pytest
from django.urls import reverse

from homepage.models import Profile

HOMEPAGE_URL = reverse("homepage")


@pytest.mark.django_db
def test_homepage_returns_200(client):
    """Test that the homepage returns a 200 status code."""
    response = client.get(HOMEPAGE_URL)
    assert response.status_code == 200


@pytest.mark.django_db
def test_homepage_uses_correct_template(client):
    """Test that the homepage uses the correct template."""
    response = client.get(HOMEPAGE_URL)
    assert "homepage.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_homepage_profile_in_context(client):
    """Test that the homepage includes the profile in the context."""
    response = client.get(HOMEPAGE_URL)
    assert "profile" in response.context


@pytest.mark.django_db
def test_homepage_displays_profile_info(client):
    """Test that the homepage displays the profile information."""
    Profile.objects.create(
        name="John Doe",
        bio="Software developer with a passion for open source.",
    )
    response = client.get(HOMEPAGE_URL)
    assert "John Doe" in response.content.decode()
    assert "Software developer with a passion for open source." in response.content.decode()


@pytest.mark.django_db
def test_homepage_no_profile(client):
    """Test that the homepage handles the case where no profile exists."""
    response = client.get(HOMEPAGE_URL)
    assert "profile" in response.context
    assert response.context["profile"] is None
