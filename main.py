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


cities = ["Ann Arbor, MI", "Athens, OH", "Bloomington, IN", "Madison, WI", "Syracuse, NY", "Berkeley, CA", "Boulder, CO", "Tempe, AZ", "Malibu, CA", "Corvallis, OR"]

city = cities[city_idx]

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
    bus_dict[business['name']] = (business['id'],business['rating'],business['price'])

for bus in bus_dict.keys():
    id1 = bus_dict[bus][0]
    rating1 = bus_dict[bus][1]
    price1 = bus_dict[bus][2]
    res_data = requests.request('GET', review_url.format(id1), headers=headers)
    parsed_data = res_data.json()
    review_data[bus] = (parsed_data['reviews'], rating1, price1, city)

for rest in review_data.keys():
    listOfReviews = []
    for review in review_data[rest][0]:
        listOfReviews.append((review['rating'], review['text']))
    review_data[rest] = list(review_data[rest])
    review_data[rest][0] = listOfReviews


with open(full_path, 'w') as outfile:
    json.dump(review_data, outfile)


print(review_data)