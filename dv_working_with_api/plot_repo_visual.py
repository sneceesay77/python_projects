import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make and API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dict = r.json()
all_repos = response_dict['items']

repo_links, stars, labels = [],[],[]
for repo in all_repos:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_links.append(f"<a href='{repo_url}'>{repo_name}")
    stars.append(repo['stargazers_count'])
    owner = repo['owner']['login']
    description = repo['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
    
    
#Make visualisation
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'marker': {'color': 'rgb(60, 100, 150)', 'line': {'width':1.5, 'color':'rgb(255,255,255)'}},
    'opacity':0.6,
    'hovertext':labels
}]

my_layout = {
    'title': 'Most Popular Python projects on Github',
    'titlefont': {'size':28},
    'xaxis': {'title': 'Repository', 'titlefont':{'size':24}, 'tickfont':{'size':14}},
    'yaxis': {'title': 'Stars', 'titlefont':{'size':24}, 'tickfont':{'size':14}},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='popular_python_repos.html')




