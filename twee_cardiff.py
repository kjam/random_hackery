import tweepy

AUTH_SECRET = 'SHHHHH'
AUTH_KEY = 'YRKEY'

auth = tweepy.OAuthHandler(AUTH_KEY, AUTH_SECRET)
api = tweepy.API(auth)

tweets = api.search('Caerdydd')

for t in tweets:
    print '{}: @{} < {} >'.format(t.created_at.strftime(
        '%d-%m-%Y %H:%M'), t.user.name, t.text)
