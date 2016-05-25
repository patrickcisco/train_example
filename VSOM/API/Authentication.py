import VSOM.client

def login(name, password):
  body = {
    "username": name,
    "password": password
  }
  client = VSOM.client.new("/authentication/login", body)
  return client.post_it()