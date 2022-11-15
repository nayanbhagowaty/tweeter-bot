import tweepy
import time
import requests
import random
import os

def PickAFFile():
  randNum = random.randrange(0,3)
  #print('fileno: ' + str(randNum))
  if randNum == 0:
    url = 'https://raw.githubusercontent.com/nayan112/books/main/Hamlet'
    fileName='Hamlet'
  elif randNum == 1:
    url = 'https://raw.githubusercontent.com/nayan112/books/main/JoyceKilmer'
    fileName='JoyceKilmer'
  elif randNum == 2:
      url = 'https://raw.githubusercontent.com/nayan112/books/main/RudyardKipling'
      fileName='RudyardKipling'
  elif randNum == 3:
      url = 'https://raw.githubusercontent.com/nayan112/books/main/OmarKhayyam'
      fileName='OmarKhayyam'

  return url, fileName

def GetFileContent(url,filename):
  #print(filename)
  #assert os.path.isfile(filename)
  exist = os.path.exists(filename)
  if not exist:
    page = requests.get(url)
    storyText = page.text
    with open(filename, "w") as f:
      f.write(storyText)
  with open(filename,'r') as f:
    txt = f.read()
  return txt

def GetTweet(storyText,filename):
  spltLines =storyText.splitlines()
  rerun = True
  i = 0
  while rerun:
    lineIndex = random.randrange(10, len(spltLines)-20)
    if len(spltLines[lineIndex + i]) < 10:
      i = i+1
    else:
      rerun = False
  return spltLines[lineIndex + i] + '\n'  + spltLines[lineIndex + i + 1] + '\n\n#'+ filename +'  #poetry'

def postTweet(tweet):
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler(os.environ['consumer_key']) #("CONSUMER_KEY", "CONSUMER_SECRET")
  auth.set_access_token(os.environ['access_token'])   #ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
  # Create API object
  api = tweepy.API(auth)
  # Create a tweet
  api.update_status(tweet)

#while True:
#  url,filename = PickAFFile()
#  content = GetFileContent(url,filename)
#  tweet = GetTweet(content,filename)
  #print(tweet)
#  if not len(tweet)<10:
#    postTweet(tweet)
#  time.sleep(6)#0*60)
#  pass

url,filename = PickAFFile()
content = GetFileContent(url,filename)
tweet = GetTweet(content,filename)
print(tweet)
if not len(tweet)<20:
  postTweet(tweet)
