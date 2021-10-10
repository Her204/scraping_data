import tweepy as tw
import pandas as pd
import datetime
import os

API_KEY = "9nwrfo5X9I3cEtBfMrm9L0gs5"

API_KEY_SECRET = "2fOeqnVrHWZKuCIKiQCxAprLs6J7ky3evFsAx88pPswJZRWAZo"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKiEIwEAAAAA2K9c81v7cKqDLn4qckgBnJApA6w%3DMgbQR3sjUlTkOxl0UKZWHvzmpqEju0JfaBtuV8ByP3kFEuaFsA"

ACCESS_TOKEN = "1317512952325472260-vaCRvBd5ydns85HyYMoNzZra5xYPZ4"

ACCESS_TOKEN_SECRET = "QKIxxBQf79nZWpBT5xTQFrA4cHbaqyInsm8YlRBOvpYWe"

auth = tw.OAuthHandler(API_KEY,API_KEY_SECRET)

auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tw.API(auth,wait_on_rate_limit=True)


search_word = input("Enter what you wanna search: ")

#data_since = "2018-05-28"

print(dir(api))
start = datetime.datetime.now()
tweets = tw.Cursor(api.search_tweets,
                   q = search_word#, 
                   #lang ='en',
 #                  since = data_since
                   ).items(500)
print(dir(tweets))
tweet_details = [[tweet.text,
                  tweet.user.screen_name,
                  tweet.user.location] for tweet in tweets]
end = datetime.datetime.now()
df = pd.DataFrame(columns=["TWEET","USER NAME","USER LOCATION"],data=tweet_details)

df.to_csv(os.getcwd()+"/tweets_from_{}.csv".format(search_word))
print(start,end)
print(df["USER LOCATION"].value_counts())
