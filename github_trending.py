import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size, days_ago=7):
    since_date_dt = datetime.now().date() - timedelta(days=days_ago)
    url = '{}'.format('https://api.github.com/search/repositories')
    response = requests.get(
        url=url,
        params={
            'q': 'created:>{since_date}'.format(
                since_date=since_date_dt.strftime('%Y-%m-%d')),
            'sort': 'stars',
            'order': 'desc'
        }
    )
    if response.ok:
        return response.json()['items'][:top_size]
    return []


def get_open_issues_amount(issues_url):
    open_issues_amount = 0
    issues_response = requests.get(issues_url.replace('{/number}', ''))
    if not issues_response.ok:
        return None
    for issue in issues_response.json():
        if not issue.get('pull_request'):
            open_issues_amount += 1
    return open_issues_amount


if __name__ == '__main__':
    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repo in trending_repositories:
        if repo['has_issues']:
            open_issues_amount = get_open_issues_amount(repo['issues_url'])
        print(
            repo['html_url'],
            repo['description'],
            ' | Open Issues: {}'.format(open_issues_amount)
        )
