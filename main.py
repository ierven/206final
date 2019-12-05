import requests
import json
import sys

sys.argv * 20


API_KEY = "aGUAFSIk5qetLlnhr5z6G93ew_cx3DYT2nT2nqeRs34n-mZVZ5j-msEqj_LvGOyU3SuXv6d45ZVbodjTnPzXuIYt-mleQEaVjATrWAKT2zPPI0hk_juoc3kGAHnoXXYx"
search_url = "https://api.yelp.com/v3/businesses/search?location=\"Ann Arbor, MI\"&radius=30000"

headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }
response = requests.request('GET', search_url, headers=headers)

data = response.json()

data1 = data.total

print(data)