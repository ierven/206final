import requests
import json
import sys

sys.argv * 20


API_KEY = "aGUAFSIk5qetLlnhr5z6G93ew_cx3DYT2nT2nqeRs34n-mZVZ5j-msEqj_LvGOyU3SuXv6d45ZVbodjTnPzXuIYt-mleQEaVjATrWAKT2zPPI0hk_juoc3kGAHnoXXYx"
search_url = "https://api.yelp.com/v3/businesses/search?location=\"Ann Arbor, MI\"&radius=30000"
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
    bus_dict[business['name']] = (business['id'],business['price'])

for bus in bus_dict.keys():
    id1 = bus_dict[bus][0]
    price1 = bus_dict[bus][1]
    res_data = requests.request('GET', review_url.format(id1), headers=headers)
    parsed_data = res_data.json()
    review_data[bus] = (parsed_data['reviews'], price1)


reviews_price_organized = {}
for restaurant in review_data.keys():
    review_price = review_data[restaurant][1]
    for review in review_data[restaurant][0]:
        reviews = []
        review_txt = review['text']
        reviews.append(review_txt)
    if review_price not in reviews_price_organized:
        reviews_price_organized[review_price] = []
    reviews_price_organized[review_price].append(reviews)
print(data)