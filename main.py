from twitter import Twitter

twitter = Twitter()

key = 'your key'
secret = 'your secret'
token_key = 'token key'
token_secret = 'token secret'

# Connection

instance = Twitter(key, secret, token_key, token_secret)

# Post Tweets
baseURL = 'your base URL'
post = 'your tweet'
response = instance.tweet(post, baseURL)

# Search Tweets

baseURL = 'your base URL'
query = 'your query'
lang = 'Language'
response = instance.search(baseURL, query, lang)


