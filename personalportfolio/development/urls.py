from django.urls import path

from . import views

urlpatterns = [
    path("", views.development, name="development"),
]
