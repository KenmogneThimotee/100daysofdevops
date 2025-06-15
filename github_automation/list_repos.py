import requests
import os
import json

data = {"type": "all", "sort":"full_name", "direction": "asc"}

username = input("Please enter your GitHub username: ")
output = requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data), timeout=60)
output = json.loads(output.text)

for reponame in output:
    print(reponame['name'])
