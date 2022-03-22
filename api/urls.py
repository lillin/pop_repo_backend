from django.urls import path

from api.views import RepoPopularitySearchView

urlpatterns = [
    path('repo-popularity', RepoPopularitySearchView.as_view()),
]
