import requests

class HttpClient(object):
    def __init__(self, url):
        if not url:
            raise Exception('A url is required')
        self.url = url

    def get(self, params):
        return requests.get(self.url, params=params)

    def post(self, data):
        return requests.post(self.url, data=data)