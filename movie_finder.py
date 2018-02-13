import requests


class MovieFinder():

    def __init__(self, your_api_url):
        #you can find your own api url key at www.omdbapi.com!
        self.url = your_api_url

    #does a content search using omdapi
    def content_search(self, movie_title):
        API_URL = self.url
        headers = {
            'User-Agent': 'chrome v1.1'
        }

        #params are simply the movie title and the type of film it is
        search_params = {
            't': movie_title,
            'type': 'movie'
        }

        #make the request
        r = requests.get(API_URL, params=search_params, headers=headers)

        #create usable json
        r = r.json()

        #needed to encode because was getting an error
        dictionary = {'title': r['Title'].encode('utf8'), 'plot': r['Plot'].encode('utf8'), 'rating': r['Ratings'][1]['Value'].encode('utf8'), 'poster': r['Poster'].encode('utf8')}
        return dictionary