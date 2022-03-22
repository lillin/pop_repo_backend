import pytest
from collections import OrderedDict

from unittest.mock import patch, Mock
from api.serializers import (
    RepoPopularitySearchSerializer,
    RepoPopularityByOwnerSerializer
)


REPO_POPULARITY_SEARCH_DATA = [
    [{'repo': 'hello'},
     {'page': 3},
     {'repo': 'hello',
      'results': {
          'search_results': [OrderedDict([('name', 'hello'), ('full_name', 'world/hello'), ('is_popular', True)])],
          'next_page': '4'}}],
]


REPO_POPULARITY_BY_OWNER = [
    [{'repo': 'hello', 'owner': 'world'},
     {'repo': 'hello', 'owner': 'world', 'result': {'name': 'hello', 'full_name': 'world/hello', 'is_popular': True}}],
]


@pytest.mark.parametrize('input_data, context, expected_output', REPO_POPULARITY_SEARCH_DATA)
@patch('requests.get')
def test_repo_popularity_search_serializer(mock_get, input_data, context, expected_output):
    response = {'items': [{
        'name': 'hello',
        'full_name': 'world/hello',
        'forks_count': 200,
        'stargazers_count': 200,
        'private': False,
        'open_issues': 10,
    }]}
    links = {
        'next': {'url': 'github/?page=4'}
    }

    mock_get.return_value = Mock()
    mock_get.return_value.links = links
    mock_get.return_value.json.return_value = response

    serializer = RepoPopularitySearchSerializer(data=input_data, context=context)

    assert serializer.is_valid()
    assert serializer.data == expected_output


@pytest.mark.parametrize('input_data, expected_output', REPO_POPULARITY_BY_OWNER)
@patch('requests.get')
def test_repo_popularity_by_owner_serializer(mock_get, input_data, expected_output):
    response = {
        'name': 'hello',
        'full_name': 'world/hello',
        'forks_count': 200,
        'stargazers_count': 200,
        'private': False,
        'open_issues': 10,
    }

    mock_get.return_value = Mock()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = response

    serializer = RepoPopularityByOwnerSerializer(data=input_data)

    assert serializer.is_valid()
    assert serializer.data == expected_output
