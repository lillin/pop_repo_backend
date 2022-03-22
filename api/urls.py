from django.urls import path

from api.views import RepoPopularitySearchView, RepoPopularityByOwnerView

urlpatterns = [
    path('repo-popularity', RepoPopularitySearchView.as_view()),
    path('repo-popularity-by-owner', RepoPopularityByOwnerView.as_view()),
]
