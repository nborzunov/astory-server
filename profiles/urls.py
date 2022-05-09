from django.urls import path
from .views import ProfileView, ListFollowerView, FollowerView

urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:pk>', FollowerView.as_view()),
    path('list', ListFollowerView.as_view())
]