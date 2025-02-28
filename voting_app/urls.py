from django.urls import path
from .views import add_candidate_view, vote_view, get_winner_view, get_balance_view, home

urlpatterns = [
    path("add_candidate/", add_candidate_view, name="add_candidate_view"),
    path("vote/", vote_view, name="vote"),
    path("get_winner/", get_winner_view, name="winner"),
    path("get_balance/", get_balance_view, name="balance"),
    path("home/", home, name="home"),
]
