"""qs_wolframalpha.py

Takes a query from [Quicksilver](https://qsapp.com) and gets it from the
Wolfram Alpha API, returns it to Quicksilver.
"""

import xml.etree.ElementTree as etree
import sys

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    # Python2
    from urllib import urlencode
    from urllib2 import urlopen

def main(appid, query):

    api_root = "http://api.wolframalpha.com/v2/"

    payload = {
        'input': query,
        'appid': appid,
        'async': 'true',
        'reinterpret': 'true'
    }
    resp = urlopen(api_root + "query?" + urlencode(payload))
    tree = etree.fromstring(resp.read())

    try:
        # Return first subpod's plaintext
        result = next(pod.find("subpod").find("plaintext").text
                      for pod in tree
                      if pod.attrib.get('title') == "Result")
    except StopIteration:
        result = "No results for {}".format(query)

    return result

if __name__ == "__main__":
    appid = sys.argv[1]
    query = sys.argv[2]
    print(main(appid, query))
