import json
import APIBase

def new(uri, body={}, token=None):
  headers = {
    "accept": "application/json",
    "content-type": "application/json"
  }
  return APIBase.Client("https://api.tropo.com/1.0", uri, headers, json.dumps(body))