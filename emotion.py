import os
import json
    
def getEmotionScores():
    filename = "words.json"
    filename2 = "reviews.json"
    filename3 = "reviewsEmotion.json"
    full_path = os.path.join(os.path.dirname(__file__), filename)
    full_path2 = os.path.join(os.path.dirname(__file__), filename2)
    full_path3 = os.path.join(os.path.dirname(__file__), filename3)

    posWords = []
    negWords = []

    with open(full_path, 'r') as words_file:
        wordsDict = json.load(words_file)

    posWords = wordsDict['pos_words']
    negWords = wordsDict['neg_words']


    def calcEmotionScore(review_in):
        review_score = 0
        reviewWords = review_in.split()
        for word in reviewWords:
            if word.lower() in posWords:
                review_score += 1
            if word.lower() in negWords:
                review_score -= 1
        return review_score

    print("calculating emotion scores...")
    with open(full_path2, 'r') as words_file:
        reviewDict = json.load(words_file)
        for rest in reviewDict.keys():
            reviews = reviewDict[rest][0]
            idx = 0
            for review in reviews:
                reviewText = review[1]
                score = calcEmotionScore(reviewText)
                reviewDict[rest][0][idx].append({'emotion': score})
                idx += 1

    print("appending emotion data to json file at {}".format(full_path3))
    for rest in reviewDict.keys():
        avgEmotion = 0
        for review in reviewDict[rest][0]:
            avgEmotion += review[2]['emotion']
        avgEmotion /= 3
        reviewDict[rest].append(avgEmotion)

    with open(full_path3, 'w') as words_file:
        json.dump(reviewDict, words_file)