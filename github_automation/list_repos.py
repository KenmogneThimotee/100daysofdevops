import os
import json
from security import safe_requests

data = {"type": "all", "sort":"full_name", "direction": "asc"}

username = input("Please enter your GitHub username: ")
output = safe_requests.get("https://api.github.com/users/{}/repos".format(username), data=json.dumps(data))
output = json.loads(output.text)

for reponame in output:
    print(reponame['name'])
