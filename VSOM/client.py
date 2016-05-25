import json
import APIBase

def new(uri, body={}, token=None):
  headers = {'x-ism-sid': token} 
  return APIBase.Client("https://171.68.22.61/ismserver/json", uri, headers, json.dumps(body), False)