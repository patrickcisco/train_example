#### Camera.py will have methods for interacting with the /camera endpoint
import VSOM.client

def get_cameras(token):
  body = {
    "filter": {
      "byObjectType": "device_vs_camera",
      "pageInfo": {
        "start": "0",
        "limit": "100"
      }
    }
  }
  client =  VSOM.client.new("/camera/getCameras", body, token)
  return client.post_it()

def get_by_name(token, name):
  body = {
    "filter": {
      "byObjectType": "device_vs_camera",
      "byExactName": name,
      "pageInfo": {
        "start": "0",
        "limit": "100"
      }
    }
  }
  client =  VSOM.client.new("/camera/getCameras", body, token)
  return client.post_it()