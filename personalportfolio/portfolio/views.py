from django.views import generic

from .models import Project


class ProjectListView(generic.ListView):
    """View for listing all published projects."""

    model = Project
    template_name = "portfolio.html"
    context_object_name = "projects"

    def get_queryset(self):
        """Return only published projects ordered by publish date."""
        return Project.objects.filter(is_published=True).order_by("-publish_date")


class ProjectDetailView(generic.DetailView):
    """View for displaying a single published project."""

    model = Project
    template_name = "project_detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        """Only allow access to published projects."""
        return Project.objects.filter(is_published=True)
