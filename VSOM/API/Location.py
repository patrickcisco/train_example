#### Location.py will have methods for interacting with the /location endpoint
import VSOM.client

def get_tree_root(token):
  body = {
    "treeFilter": {
      "objectTypes": [],
      "depth": 0,
      "getLocalTreeOnly": False
    }
  }
  client = VSOM.client.new("/location/getLocationTree", body, token)
  return client.post_it()