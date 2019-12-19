# Created by Isaiah Erven and Puyan Gholizadeh

import requests
import json
import os
import sys
import thesInit
import reviewdb
import wordsdb
import yelpInit
import emotion

cur, conn = reviewdb.setUpDatabase('Yelp_Restaurants.db')

try:
    args = sys.argv
except:
    print("command line args failed")

if len(args) > 1 and args[1] == "--init":
    print("Project for team We Love SI 206 by Puyan and Isaiah")
    print("Project goal: Compare yelp data for different college towns in the USA")
    thesInit.getWordsMerriamAPI()
    print("Merriam Webster Data Initialized")
    print("reading data and writing to database")
    json_data = reviewdb.readDataFromFile('wordsdb.json')

    wordsdb.createWordsDBS(json_data, cur, conn)
    print("created words tables")
    print("please run the same command with values 0-10 instead of --init to gather city data")

elif len(args) > 1 and args[1] = "--help":
    print("run the file with --init to initialize the data required to perform the emotion score rating")
    print("run the file with values 0, 1, 2... 8, 9, 10 to gather review data")
    print("run the visualizations and calculations file to manipulate and display data")

elif len(args) > 1 and int(args[1]) < 11:
    city_idx = args[1]

    cities = ["Ann Arbor, MI", "Athens, OH", "Bloomington, IN", "Ames, IA", "Syracuse, NY", "Berkeley, CA", "Los Angeles, CA", "Boulder, CO", "Tempe, AZ", "Malibu, CA", "Corvallis, OR"]
    city = cities[int(city_idx)]

    yelpInit.getCityData(city)

    #calculate emotion score and append it to json file
    emotion.getEmotionScores()

    print("data collection/processing complete")

    #insert yelp data into database
    json_data = reviewdb.readDataFromFile('reviewsEmotion.json')
    #try:
    reviewdb.insertIntoDB(json_data, cur, conn, city_idx, cities)
    print("review data successfully inserted")
    # except:
    #     print("failed to insert review data")
    print("run complete")