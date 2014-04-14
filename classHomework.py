import nltk
import urllib
import random
import json
class SentenceSwitch(object):
		def __init__(self, sentence, apiKey):
			self.sentence = sentence
			self.apiKey = apiKey
		def returnPOS(self):   
			token = nltk.word_tokenize(self.sentence)
			PartOfSpeech = list()
			for i in nltk.pos_tag(token):
				PartOfSpeech.append(i[1])
			return PartOfSpeech

		def returnToken(self):
			token = nltk.word_tokenize(self.sentence)
			TokenWords =list()
			for i in nltk.pos_tag(token):
				TokenWords.append(i[0])
			return TokenWords

		def checkPOS(self, word):
			return nltk.pos_tag(nltk.word_tokenize(word))[0][1]

		def replaceWord(self, iterations):
			word = self.returnToken()
			pos = self.returnPOS()
			newSentence = list()
			for i in range(len(word)):
				mWord = word[i]
				mPos = pos[i]
				interations = iterations
				if len(mWord)>2 and mPos is not None:
					types =['related-word', 'synonym' , 'antonym' ,'same-context','hypernym']
					params = {
						'useCanonical': 'true',
						'relationshipTypes' : types[random.randrange(5)],
						'limitPerRelationshipType': '10',
						'api_key': self.apiKey
						}
					url = "http://api.wordnik.com/v4/word.json/" + urllib.quote_plus(mWord) \
					+"/relatedWords?" + urllib.urlencode(params)
					urlobj = urllib.urlopen(url)
					result = json.loads(urlobj.read())
					if len(result) > 0:
						for definition in result:
							count = 0
							while True:
								newWord = definition['words'][random.randrange(len(definition['words']))]
								count+=1
								if self.checkPOS(newWord) == mPos:
									newSentence.append(newWord)
									break
								elif count>iterations:
									newSentence.append(mWord)
									break
					else:
					 	newSentence.append(mWord)
					 		
				else:
					newSentence.append(mWord)
			return newSentence

		

