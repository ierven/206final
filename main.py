import requests
import json
import os

filename = "reviews.json"
filename_count = "count.json"
full_path = os.path.join(os.path.dirname(__file__), filename)
full_path_count = os.path.join(os.path.dirname(__file__), filename_count)

with open(full_path_count, 'r') as count_file:
    fileData = json.load(count_file)
    city_idx = fileData['count']


cities = ["Ann Arbor, MI", "Athens, OH", "Bloomington, IN", "Ames, IA", "Syracuse, NY", "Berkeley, CA", "Los Angeles, CA", "Boulder, CO", "Tempe, AZ", "Malibu, CA", "Corvallis, OR"]

city = cities[city_idx]
with open(full_path_count, 'w') as count_file:
    fileData['count'] += 1
    json.dump(fileData, count_file)

API_KEY = "aGUAFSIk5qetLlnhr5z6G93ew_cx3DYT2nT2nqeRs34n-mZVZ5j-msEqj_LvGOyU3SuXv6d45ZVbodjTnPzXuIYt-mleQEaVjATrWAKT2zPPI0hk_juoc3kGAHnoXXYx"
search_url = "https://api.yelp.com/v3/businesses/search?location=\"{}\"&radius=30000".format(city)
review_url = "https://api.yelp.com/v3/businesses/{}/reviews"

headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }
response = requests.request('GET', search_url, headers=headers)

data = response.json()

data2 = data['businesses']
bus_dict = {}

review_data = {}
for business in data2:
    if 'price' in business.keys():
        bus_dict[business['name']] = (business['id'],business['rating'],business['price'])

for bus in bus_dict.keys():
    id1 = bus_dict[bus][0]
    rating1 = bus_dict[bus][1]
    price1 = bus_dict[bus][2]
    res_data = requests.request('GET', review_url.format(id1), headers=headers)
    parsed_data = res_data.json()
    if 'reviews' in parsed_data.keys():
        review_data[bus] = (parsed_data['reviews'], rating1, price1, city)

for rest in review_data.keys():
    listOfReviews = []
    for review in review_data[rest][0]:
        listOfReviews.append((review['rating'], review['text']))
    review_data[rest] = list(review_data[rest])
    review_data[rest][0] = listOfReviews


with open(full_path, 'w') as outfile:
    json.dump(review_data, outfile)



#calculate emotion score and append it to json file

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

for rest in reviewDict.keys():
    avgEmotion = 0
    for review in reviewDict[rest][0]:
        avgEmotion += review[2]['emotion']
    avgEmotion /= 3
    reviewDict[rest].append(avgEmotion)

with open(full_path3, 'w') as words_file:
    json.dump(reviewDict, words_file)

print("run complete")