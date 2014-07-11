# -*- coding: utf-8 -*-

import config
from .http_client import HttpClient

class Yo(object):
    def __init__(self, api_token=None):
        if not api_token:
            raise Exception('An API Token is required')
        self.api_token = api_token
        self.http_client = HttpClient(config.YO_URL)

    def yo(self, username=None):
        data = {}
        data['api_token'] = self.api_token
        if username:
            data['username'] = username
        return self.http_client.post(data)
