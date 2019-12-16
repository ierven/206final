import os
import sqlite3
import json

def readDataFromFile(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

json_data = readDataFromFile('wordsdb.json')
cur, conn = setUpDatabase('Yelp_Restaurants.db')


# cur.execute('DROP TABLE IF EXISTS Positive_Words')
# cur.execute('CREATE TABLE Positive_Words (original_word TEXT, synonym TEXT)')

# cur.execute('DROP TABLE IF EXISTS Negative_Words')
# cur.execute('CREATE TABLE Negative_Words (original_word TEXT, synonym TEXT)')

review_keys = json_data.keys()
review_keys = list(review_keys)
print(len(review_keys))

pos_root_wrds = json_data['pos_words'].keys()
neg_root_wrds = json_data['neg_words'].keys()

pst_words = []
for word_root in pos_root_wrds:
    lst_words = json_data['pos_words'][word_root]
    for synonym in lst_words:
        pst_words.append((word_root, synonym))
print(pst_words)

neg_words = []
for word_root in neg_root_wrds:
    lst_words = json_data['neg_words'][word_root]
    for synonym in lst_words:
        neg_words.append((word_root, synonym))
print(neg_words)

for i in range(100, 120):
    cur.execute('INSERT INTO Negative_Words (original_word, synonym) VALUES (?, ?)',
        (neg_words[i][0], neg_words[i][1]))
conn.commit()