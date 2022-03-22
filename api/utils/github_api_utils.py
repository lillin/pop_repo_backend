from typing import Dict, Tuple, Any, Optional

import requests
from django.conf import settings


def get_next_page(links):
    next_page = links.get('next')
    return next_page['url'].split('=')[-1] if next_page else None


def search_by_repo_name(name: str, page: int = 1) -> Tuple[Any, Optional]:
    """
    Searches GitHub repositories by name from the given string.
    """
    resource = \
        f'{settings.GITHUB_API_DOMAIN}/search/repositories?q={name}+in:name&per_page={settings.PAGE_SIZE}&page={page}'
    headers = {
        'Authorization': f'token {settings.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3.text-match+json',
    }
    response = requests.get(resource, headers=headers)

    return response.json(), get_next_page(response.links)


def get_by_repo_name(name: str, owner: str) -> Dict:
    """
    Get repository from the given owner and repository name.
    """
    resource = f'{settings.GITHUB_API_DOMAIN}/repos/{owner}/{name}'
    headers = {
        'Authorization': f'token {settings.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(resource, headers=headers)

    return response.json() if response.status_code < 400 else {}
