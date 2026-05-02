"""
Tests for homepage models.
"""

import pytest
from django.core.exceptions import ValidationError

from homepage.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """Test the string representation of the Profile model."""
    profile = Profile.objects.create(
        name="John Doe",
        bio="Software developer with a passion for open source.",
    )
    assert str(profile) == "John Doe"


@pytest.mark.django_db
def test_profile_fields():
    """Test the fields of the Profile model."""
    profile = Profile.objects.create(
        name="Jane Smith",
        bio="Data scientist with expertise in machine learning.",
        github_url="https://github.com/janesmith",
        linkedin_url="https://linkedin.com/in/janesmith",
        email="jane.smith@example.com",
    )
    assert profile.name == "Jane Smith"
    assert profile.bio == "Data scientist with expertise in machine learning."
    assert profile.github_url == "https://github.com/janesmith"
    assert profile.linkedin_url == "https://linkedin.com/in/janesmith"
    assert profile.email == "jane.smith@example.com"


@pytest.mark.django_db
def test_profile_blank_fields():
    """Test that blank fields in the Profile model are handled correctly."""
    profile = Profile.objects.create(
        name="Alice Johnson", bio="Full-stack developer with a focus on frontend technologies."
    )
    assert profile.name == "Alice Johnson"
    assert profile.bio == "Full-stack developer with a focus on frontend technologies."
    assert profile.github_url == ""
    assert profile.linkedin_url == ""
    assert profile.email == ""


@pytest.mark.django_db
def test_profile_name_required():
    """Profile should fail validation if name is empty."""
    profile = Profile(name="", bio="Some bio")
    with pytest.raises(ValidationError):
        profile.full_clean()


@pytest.mark.django_db
def test_profile_bio_required():
    """Profile should fail validation if bio is empty."""
    profile = Profile(name="Jane Dev", bio="")
    with pytest.raises(ValidationError):
        profile.full_clean()


@pytest.mark.django_db
def test_profile_name_max_length():
    """Profile should fail validation if name exceeds max length."""
    long_name = "A" * 101  # 101 characters
    profile = Profile(name=long_name, bio="Some bio")
    with pytest.raises(ValidationError):
        profile.full_clean()
