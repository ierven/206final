import requests
import json
import os


filename = "words.json"
full_path = os.path.join(os.path.dirname(__file__), filename)

thesKey = "31d9d27b-4af0-4573-b493-842b62cc47d1"
url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=31d9d27b-4af0-4573-b493-842b62cc47d1"

posWords = ["great", "excellent", "stellar", "delicious", "fast", "tasty", "flavorful", "nice", "fun", "welcoming", "clean", "efficient", "good", "wonderful"]
posWordsExtended = []
posWordsDict = {}

for word in posWords:
    url_word = url.format(word)
    goodData = requests.get(url_word).json()
    syns = goodData[0]['meta']['syns'][0]
    for word in syns:
        if word not in posWordsExtended:
            posWordsExtended.append(word)

posWordsDict["words"] = posWordsExtended

with open(full_path, 'w') as outfile:
    json.dump(posWordsDict, outfile)
print(posWordsExtended)
