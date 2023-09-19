```py
#Imports the dependancies on the request
import requests 

#Imports the dependencies of the json
import json

# Url link of the API
url = "https://anapioficeandfire.com/api/characters"

# HTTP method to get the  characters
response = requests.get(url)

#Loads the http verb that we have provided
json_content = json.loads (response.text)

#prints the message from the response.text
print(json.dumps(json_content, indent = 4))
```
