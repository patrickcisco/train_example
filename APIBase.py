import requests
import json

class Client(object):
    def __init__(self, host, uri, headers={}, body={}, verify=True):
      self.__host  = host
      self.uri     = uri
      self.body    = body
      self.headers = headers
      self.verify  = verify

    def get_it(self):
      r = requests.get(self.__host + self.uri, headers=self.headers, verify=self.verify)
      return r.json()

    # we will use post_it() for sending a post request
    # and returing a json representaion of the corresponding http response's body
    def post_it(self):
      r = requests.post(self.__host + self.uri, headers=self.headers, data=self.body, verify=self.verify)
      return r.json()

    # we will use post() for sending a post request
    # and returing the corresponding http response
    def post(self):
      r = requests.post(self.__host + self.uri, headers=self.headers, data=self.body, verify=self.verify)
      return r