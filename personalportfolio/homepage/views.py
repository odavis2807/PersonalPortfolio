"""
Views for the homepage app.
"""

from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Profile


class HomepageView(generic.TemplateView):
    """View for the homepage."""

    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        """
        Add the Profile instance with primary key 1 to the context as 'profile'.
        Raises a 404 error if the Profile does not exist.
        """
        context = super().get_context_data(**kwargs)
        context["profile"] = get_object_or_404(Profile, pk=1)
        return context
