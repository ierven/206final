import requests
import json
import os


# REQUIRES: Null (No parameters)
# MODIFIES: Modifies JSON files containing word data from Merriam Webster API
# EFFECTS: Makes requests to Merriam Webster API to obtain synonyms
#          Appends list of positive/negative words to be used in emotion score calculation
#          Writes word data to JSON files to be used in emotion calculation and db storage

def getWordsMerriamAPI():
    #store json filenames to be created/written to
    print("Beginning Merriam API interaction...")
    filename = "words.json"
    filename2 = "wordsdb.json"
    full_path = os.path.join(os.path.dirname(__file__), filename)
    full_path2 = os.path.join(os.path.dirname(__file__), filename2)

    #store url with {} to format the word into the url
    thesKey = "31d9d27b-4af0-4573-b493-842b62cc47d1"
    url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=31d9d27b-4af0-4573-b493-842b62cc47d1"

    #use list of positive root words to make request to database for synonyms
    #append new positive words to positive words list
    posWords = ["friendly", "fresh", "awesome", "kind", "hype", "super", "unique","gourmet", "ambiance", "glad", "healthy", "comfortable", "favorite", "top","haven", "love", "impressed", "great", "excellent", "stellar", "delicious", "fast", "tasty", "flavorful", "nice", "fun", "welcoming", "clean", "efficient", "good", "wonderful", "best", "enjoyable"]
    posWordsDict = {}
    posWordsExtended = []
    wordsDict = {}
    print("requesting Merriam data...")
    for word in posWords:
        posWordsExtended.append(word)
    for word in posWords:
        url_word = url.format(word)
        goodData = requests.get(url_word).json()
        syns = goodData[0]['meta']['syns'][0]
        posWordsDict[word] = syns
        for word in syns:
            if word not in posWordsExtended:
                posWordsExtended.append(word)

    wordsDict["pos_words"] = posWordsExtended

    #use list of negative root words to make request to database for synonyms
    #append new negative words to negative words list
    negWords = ["disappointed", "sad", "bottom", "bad", "horrible", "yucky", "terrible", "rotten", "slow", "disgusting", "rude", "mean", "cold", "boring", "expensive", "awful", "poor", "worst", "closed"]
    negWordsExtended = []
    negWordsDict = {}
    
    print("parsing Merriam data...")
    for word in negWords:
        negWordsExtended.append(word)
    for word in negWords:
        url_word = url.format(word)
        badData = requests.get(url_word).json()
        syns = badData[0]['meta']['syns'][0]
        negWordsDict[word] = syns
        for word in syns:
            if word not in posWordsExtended:
                negWordsExtended.append(word)
    wordsDict["neg_words"] = negWordsExtended

    #Create dictionaries of words to be written as JSON
    wordsDictDB = {}
    wordsDictDB["pos_words"] = posWordsDict
    wordsDictDB["neg_words"] = negWordsDict

    #Write JSON data to JSON DB file and JSON words file
    print("writing Merriam data to json files")
    with open(full_path, 'w') as outfile:
        json.dump(wordsDict, outfile)

    with open(full_path2, 'w') as outfile:
        json.dump(wordsDictDB, outfile)
    print("Merriam data in json files")
