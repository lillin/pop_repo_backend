from django.conf import settings
from rest_framework import serializers

from api.utils.github_api_utils import search_by_repo_name


class GitHubSearchResultsSerializer(serializers.Serializer):
    name = serializers.CharField()
    full_name = serializers.CharField()
    forks_count = serializers.IntegerField(write_only=True)
    stargazers_count = serializers.IntegerField(write_only=True)
    is_popular = serializers.SerializerMethodField()

    def get_is_popular(self, attr):
        score = attr['stargazers_count'] + attr['forks_count'] * 2
        return True if score >= settings.REPO_SCORE else False


class RepoPopularitySearchSerializer(serializers.Serializer):
    repo = serializers.CharField(required=True, trim_whitespace=True)
    results = serializers.SerializerMethodField()

    def get_results(self, attr):
        repo_info, next_page = search_by_repo_name(attr['repo'], page=self.context.get('page'))

        search_results_serializer = GitHubSearchResultsSerializer(data=repo_info.get('items', []), many=True)
        search_results_serializer.is_valid(raise_exception=True)
        return {"search_results": search_results_serializer.data, "next_page": next_page}
