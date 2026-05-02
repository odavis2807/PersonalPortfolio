from django.db import models


class Profile(models.Model):
    """Model for homepage profile information."""

    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile/images/", blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    resume = models.FileField(upload_to="profile/resumes/", blank=True)

    def __str__(self):
        return self.name
