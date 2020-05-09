from operator import itemgetter
import requests

#Make an API call
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:50]:
    #Make a seperate API call both the f and concatenation should work
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} \t status: {r.status_code}")
    response_dict = r.json()
    
    #Build a dictionary for each article
    try:
        title = response_dict['title']
        comments = response_dict['descendants']
    except KeyError:
        print(f"Problem processing {submission_id}")
    else:
        submission_dict = {
            'title': title,
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': comments,
        }
    
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
    
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    