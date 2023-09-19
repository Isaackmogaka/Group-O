import requests

import json

url = "https://anapioficeandfire.com/api/characters"

response = requests.get(url)

json_content = json.loads (response.text)

print(json.dumps(json_content, indent = 4))