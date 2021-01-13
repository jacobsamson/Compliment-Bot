import tweepy

consumer_key = '1gWDXc3KIPeTkUDZowLKIDd4G'
consumer_secret = '9XMeNAsxY5S7Z6fD36bpJX6wkMzWD9NKU4YTxfnL0oQOe4sDRk'

key = '1332114509230604294-T17c7nuR0Mz92ISMTLWxrkYVKpSt4a'
secret = 'mWbyRQSTwvKfeCHkpxgq0B6lPTUTVN8SCFtXHnrcgA1aK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('Twitter bot working test2 -jacob')
