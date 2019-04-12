import requests
import json


class PostRequest:

    def __init__(self, url, headers, params, data):

        self.url = url
        self.headers = headers
        self.params = params
        self.data = data

    def post_data(self):

        r = requests.post(self.url, headers=self.headers, data=self.data)

        if r.status_code == 202:

            return True

        if r.status_code == 500:

            return False
