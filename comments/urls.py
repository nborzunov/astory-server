from django.urls import path
from .views import CommentView

urlpatterns = [
    path("", CommentView.as_view()),
    path("<slug:post_slug>/", CommentView.as_view()),
]