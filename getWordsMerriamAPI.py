import requests
import json
import os


filename = "words.json"
full_path = os.path.join(os.path.dirname(__file__), filename)

thesKey = "31d9d27b-4af0-4573-b493-842b62cc47d1"
url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=31d9d27b-4af0-4573-b493-842b62cc47d1"

posWords = ["friendly", "fresh", "awesome", "kind", "hype", "super", "unique","gourmet", "ambiance", "glad", "healthy", "comfortable", "favorite", "top","haven", "love", "impressed", "great", "excellent", "stellar", "delicious", "fast", "tasty", "flavorful", "nice", "fun", "welcoming", "clean", "efficient", "good", "wonderful", "best", "enjoyable"]
posWordsExtended = []
wordsDict = {}

for word in posWords:
    posWordsExtended.append(word)
for word in posWords:
    url_word = url.format(word)
    goodData = requests.get(url_word).json()
    syns = goodData[0]['meta']['syns'][0]
    for word in syns:
        if word not in posWordsExtended:
            posWordsExtended.append(word)

wordsDict["pos_words"] = posWordsExtended

negWords = ["disappointed", "sad", "bottom", "bad", "horrible", "yucky", "terrible", "rotten", "slow", "disgusting", "rude", "mean", "cold", "boring", "expensive", "awful", "poor", "worst", "closed"]
negWordsExtended = []

for word in negWords:
    negWordsExtended.append(word)
for word in negWords:
    url_word = url.format(word)
    badData = requests.get(url_word).json()
    syns = badData[0]['meta']['syns'][0]
    for word in syns:
        if word not in posWordsExtended:
            negWordsExtended.append(word)
wordsDict["neg_words"] = negWordsExtended

with open(full_path, 'w') as outfile:
    json.dump(wordsDict, outfile)
print(posWordsExtended)