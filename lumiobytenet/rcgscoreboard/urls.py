from django.urls import path
from . import views

urlpatterns = [
    path("", views.leaderboard_redirect_view, name = "Redirect to leaderboard"),
    path("<int:level_selected>/", views.leaderboard_view, name = "Leaderboard"),
    path("api/add", views.add_score_endpoint, name = "Add Score API"),
    path("api/ping", views.ping_endpoint, name = "Connection Check")
]