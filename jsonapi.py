import requests, json

endpoint = "https://api.github.com/users/pongem/repos"

repos = json.loads(requests.get(endpoint).text)

print([repo['full_name'] for repo in repos])

