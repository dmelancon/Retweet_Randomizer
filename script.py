import sys
from SentenceSwitch import SentenceSwitch

api_key = sys.argv[1]
# files = sys.argv[1]
# text = open(files)
i= 0
firstline = list()
sentenceList = list()

def rejoin(sentenceToken):
	newSentence = " ".join(sentenceToken).replace(' ,', ',')
	newSentence = newSentence.replace(' .', '.')
	return newSentence



# for line in text:          
# 	firstLine = SentenceSwitch(line, api_key)
# 	mSentence = rejoin(firstLine.replaceWord(10))
# 	for i in range(5):
# 		newLine = SentenceSwitch(mSentence, api_key)
# 		mSentence = rejoin(newLine.replaceWord(10))
# 	print mSentence

import sys
import time
import twython

Twitter_api_key="XXX"
api_secret="XXX"
access_tokenΩΩ"XXX"
token_secret= "XXX"

twitter = twython.Twython(Twitter_api_key, api_secret, access_token, token_secret)
response = twitter.get_user_timeline(screen_name='TWITTER_NAME', count=1)


for tweet in response:  
	line = tweet['text']
	#print line
	firstLine = SentenceSwitch(line, api_key)
	mSentence = rejoin(firstLine.replaceWord(10))
	for i in range(5):
		newLine = SentenceSwitch(mSentence, api_key)
		mSentence = rejoin(newLine.replaceWord(10))
	twitter.update_status(status=mSentence)
