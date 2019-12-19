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

# Main file
# REQUIRES: command line arguments --help, --init, value 0-10
# MODIFIES: creates .db file, JSON files, modifies all of the created files
# EFFECTS: reads data from 2 APIs, and creates JSON files/.db files with processed data

cur, conn, dbLoc = reviewdb.setUpDatabase('Yelp_Restaurants.db')

#try to read in command line arguments, print statement if error
try:
    args = sys.argv
except:
    print("command line args failed")

#initialize json files and get Merriam Webster data when --init command is run
if len(args) > 1 and args[1] == "--init":
    print("Project for team We Love SI 206 by Puyan and Isaiah")
    print("Project goal: Compare yelp data for different college towns in the USA")

    #get merriam webster api data
    thesInit.getWordsMerriamAPI()
    print("Database initialized")
    print(dbLoc)
    print("Merriam Webster Data Initialized")
    print("reading data and writing to database")
    json_data = reviewdb.readDataFromFile('wordsdb.json')

    #create words database
    wordsdb.createWordsDBS(json_data, cur, conn)
    print("created words tables")
    print("please run the same command with values 0-10 instead of --init to gather city data")

#print out directions if --help command is run
elif len(args) > 1 and args[1] == "--help":
    print("run the file with --init to initialize the data required to perform the emotion score rating")
    print("run the file with values 0, 1, 2... 8, 9, 10 to gather review data")
    print("run the visualizations and calculations file to manipulate and display data")

#if command line arg is integer value, use that value for index of cities list
elif len(args) > 1 and int(args[1]) < 11:
    city_idx = args[1]

    cities = ["Ann Arbor, MI", "Athens, OH", "Bloomington, IN", "Ames, IA", "Syracuse, NY", "Berkeley, CA", "Los Angeles, CA", "Boulder, CO", "Tempe, AZ", "Malibu, CA", "Corvallis, OR"]
    city = cities[int(city_idx)]

    #get city data using getCityData function
    yelpInit.getCityData(city)

    #calculate emotion score and append it to json file
    emotion.getEmotionScores()

    print("data collection/processing complete")

    #insert yelp data into database
    json_data = reviewdb.readDataFromFile('reviewsEmotion.json')
    reviewdb.insertIntoDB(json_data, cur, conn, city_idx, cities)
    print("review data successfully inserted")
    print("run complete")
    if int(args[1]) == 10:
        print("all data collected: please view .json files and .db file")
        print("run visualization and calculation file to view 'pretty' data")
else:
    print("run the file with --help for usage instructions")