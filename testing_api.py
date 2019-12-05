import requests

base_url = "https://api.datamuse.com/words?ml=good"
base_url2 = "https://api.datamuse.com/words?ml=appetizing"
base_url3 = "https://api.datamuse.com/words?ml=positive"
base_url4 = "https://api.datamuse.com/words?ml=tasty"
base_url5 = "https://api.datamuse.com/words?ml=excellent"
base_url6 = "https://api.datamuse.com/words?ml=juicy"
base_url7 = "https://api.datamuse.com/words?ml=awesome"

res1 = requests.get(base_url).json()
res2 = requests.get(base_url2).json()
res3 = requests.get(base_url3).json()
res4 = requests.get(base_url4).json()
res5 = requests.get(base_url5).json()
res6 = requests.get(base_url6).json()
res7 = requests.get(base_url7).json()


print(res1)