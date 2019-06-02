#This code downloads the tweets from twitter and stores them in a JSON file
import json
from twitter import *
from twitter.oauth import OAuth, read_token_file, write_token_file

oauth_token = "972712446040293376-eEzFseLWJM0svdT0Tzy2l2ZUfZPHeFH"
oauth_token_secret ="fMKzhxWbJfyZIAWRRfflY9PilSKtQKdrc42JfDD6SmhzX"

consumer_key="2Sp2oPacp0hZOJbBbzDxu2o8u"
consumer_secret="cwrd6UiuelgQ0cszKGfKQKazGGgwgiKS8W7csya1Kw0YpLoCEI"


t = Twitter(auth=OAuth(oauth_token,oauth_token_secret,consumer_key,consumer_secret),secure=True,format='json')

all=t.search.tweets(q="#AvengersEndgame",count=1)
print(all)
all=t.search.tweets(q="#AvengersEndgame",count=1,max_id=all["statuses"][0]["id"])
file =open("f2.json","a",encoding="utf8")
file.write(json.dumps(all))
6363
file.close()

#To extend the code for downloading several tweets (For eg 100)
#add a loop
#for i in range(100):
