import requests

URL = 'https://opentdb.com/api.php?amount=50&type=boolean'


def request_API(url):
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()['results']


question_data = request_API(URL)




