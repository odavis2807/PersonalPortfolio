"""
Views for the homepage app.
"""

from django.views import generic

from .models import Profile


class HomepageView(generic.TemplateView):
    """View for the homepage."""

    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the homepage, including the profile information.
        """
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context
