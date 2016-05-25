#### Session.py will have methods for interacting with 
#### the /sessions endpoint
import Tropo.client

def send(token, numbers, message):
  body = {
    "token": token,
    "phone_numbers": numbers,
    "the_message": message
  }
  client = Tropo.client.new("/sessions", body)
  return client.post_it()
  
