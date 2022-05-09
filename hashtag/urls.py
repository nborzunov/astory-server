from django.urls import path
from .views import TagDetailView, TagView

urlpatterns = [
    path("", TagView.as_view()),
    path("<slug:tag_slug>/", TagDetailView.as_view()),
]