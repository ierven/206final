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


#if count <= 4: 
# cur.execute('DROP TABLE IF EXISTS East_Coast_Rests')
# cur.execute('CREATE TABLE East_Coast_Rests (restaurant_name TEXT, price TEXT, rating REAL, review_1 TEXT, review_2 TEXT, review_3 TEXT, city TEXT, agg_rate REAL)')
#elif count >= 5:
# cur.execute('DROP TABLE IF EXISTS West_Coast_Rests')
# cur.execute('CREATE TABLE West_Coast_Rests (restaurant_name TEXT, price TEXT, rating REAL, review_1 TEXT, review_2 TEXT, review_3 TEXT, city TEXT, agg_rate REAL)')
def insertIntoDB (json_data, cur, conn):
    review_keys = json_data.keys()
    review_keys = list(review_keys)
    print(len(review_keys))

    for i in range(20):
        res = review_keys[i]
        agg_rating = json_data[res][-1]
        city = json_data[res][3]
        price = json_data[res][2]
        rating = json_data[res][1]
        review_1 = json_data[res][0][0][1]
        review_2 = json_data[res][0][1][1]
        review_3 = json_data[res][0][2][1]
        cur.execute('INSERT INTO West_Coast_Rests (restaurant_name, price, rating, review_1, review_2, review_3, city, agg_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (res, price, rating, review_1, review_2, review_3, city, agg_rating))
        conn.commit()
