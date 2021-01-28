'''
    From python crash course
    working with apis
'''
import requests


# make a api call and store the resposne
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.vs+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# store response in variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# explore info about repos
repo_dicts = response_dict['items']
print(f'Repositories return: {len(repo_dicts)}')

# print summary of repos
print('\nSelected info about repos:')
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")


# process results
print(response_dict.keys())
