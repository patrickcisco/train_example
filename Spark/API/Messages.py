#### Messages.py will have methods for interacting with 
#### the /message endpoint
import Spark.client

def send(token, text, files, room_id, to_person_id, to_person_email):
  body = {}
  if text != None:
    body["text"] = text
  if files != None:
    body["files"] = files
  if room_id != None:
    body["roomId"] = room_id
  if to_person_id != None:
    body["toPersonId"] = to_person_id
  if to_person_email != None:
    body["toPersonEmail"] = to_person_email
  client = Spark.client.new("/messages", body, token)
  return client.post_it()
  
