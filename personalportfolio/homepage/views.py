"""
Views for the homepage app.
"""

from django.http import HttpResponse


def homepage(request):
    """View for the homepage."""
    return HttpResponse("Welcome to my personal portfolio website!")
