import requests

class MovieFinder():

    def __init__(self, your_api_url):
        #you can find your own api url key at www.omdbapi.com!
        self.url = your_api_url

    def content_search(self, movie_title):
        API_URL = self.url
        headers = {
            'User-Agent': 'chrome v1.1'
        }

        search_params = {
            't': movie_title,
            'type': 'movie'
        }

        r = requests.get(API_URL, params=search_params, headers=headers)
        r = r.json()
        dictionary = {'title': r['Title'], 'plot': r['Plot'], 'rating': r['Ratings'][1]['Value'], 'poster': r['Poster']}
        return dictionary