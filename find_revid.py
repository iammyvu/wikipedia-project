import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests

def find_revid(url):
    parsed = urlparse.urlparse(url)
    q = (parse_qs(parsed.query)['oldid'])
    if True:
        print(q)
    else:
        raise KeyError('invalid url')

find_revid('https://en.wikipedia.org/w/index.php?oldid=935784560')


def revid_to_qid(revid, lang):
    lang = "en"
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "prop": "pageprops",
        "revids": "revid",
        "format": "json"
        }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    qid = DATA["query"]["pages"]["29828568"]["pageprops"]["wikibase_item"]
    jprint(qid)


revid_to_qid(935784560, "en")