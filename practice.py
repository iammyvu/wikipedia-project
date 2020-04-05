import json
import requests

def jprint(obj): #function to make json dict easier to read.
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "pageprops",
    "revids": "935784560",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA["query"]["pages"]["29828568"]["pageprops"]["wikibase_item"])


