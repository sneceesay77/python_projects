import requests

#Make and API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dict = r.json()

#Print results
#print(response_dict.keys())

print(f"Total Repos: {response_dict['total_count']}")
print(f"Repositories Returned: {len(response_dict['items'])}")

#get first repo and print details
all_repos = response_dict['items']
first_repo = all_repos[0]

# print(f"\nKeys: {len(first_repo)}")
# for key in sorted(first_repo.keys()):
#     print(key)
print("============================================")
for repo in all_repos:
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}\n\n")
