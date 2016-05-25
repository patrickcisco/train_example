import json
import APIBase

def new(uri, body={}, token=None):
  headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json; charset=utf-8"
  }
  return APIBase.Client("https://api.ciscospark.com/v1", uri, headers, json.dumps(body))