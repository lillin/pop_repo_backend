import requests
from django.conf import settings


def search_by_repo_name(name, page=1):
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

    next_page = response.links.get('next')
    next_page_num = next_page['url'].split('=')[-1] if next_page else None

    return response.json(), next_page_num
