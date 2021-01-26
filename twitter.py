import oauth2
import urllib.parse
import json

class Twitter:

  def __init__(self, key, secret, token_key, token_secret):
    self.connect(self, key, secret, token_key, token_secret)


  def connect(self, key, secret, token_key, token_secret):
    self.consumer = oauth2.Consumer(key, secret)
    self.token = oauth2.Token(token_key, token_secret)
    self.client = oauth2.Client(self.consumer, self.token)
    return self.client

  def tweet(self, post, baseURL):
    query = urllib.parse.quote(post, safe='')
    request = self.client.request(baseURL + query, method='POST')
    decode = request[1].decode()
    response = json.loads(decode)
    return response

  def search(self, baseURL, query, lang):
    params = urllib.parse.quote(query, safe='')
    request = self.client.request(baseURL + params + '&lang=' lang)
    decode = request[1].decode()
    response = json.loads(decode)
    twittes = response['statuses']
    return twittes
  
