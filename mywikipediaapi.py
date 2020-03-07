import requests


API_URL = 'https://en.wikipedia.org/w/api.php'


def get_wiki_urls(query, session=None):
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": query,
        "format": "json"
    }

    if session:
        resp = session.get(url=API_URL, params=params)
    else:
        resp = requests.get(url=API_URL, params=params)

    return resp.json()[3]


if __name__ == '__main__':
    result = get_wiki_urls('Russia')[0]
    print(result)