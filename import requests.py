
import requests


import json
import pprint
url = "https://api.tvmaze.com/singlesearch/shows" 
params = {"q":"Grils"}
response = requests.get(url,params)
if response.status_code == 200:
    data = json.loads(response.text)
  # pprint.pprint(data)
  name = data ['name']
  premiered = data['premiered']
    summary = data['summary']

 print (f"{name} permiered on {prmiered}.")
 print (summary)
else:
    print(f"Error: {response.status_code}")
