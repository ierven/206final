import os
import sqlite3
import json
import matplotlib.pyplot as plt


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    print("database location: " + str(path))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


cur, conn = setUpDatabase('Yelp_Restaurants.db')

def getEastTotalAggregrate(cur, conn):
    cur.execute('SELECT * FROM East_Coast_Rests')
    total = 0
    num_res = 0
    for row in cur:
        total += row[7]
        num_res += 1
    avg_agg_rating = total/num_res
    f = open("CalcFiles.txt", "w+")
    f.write("East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating))
    f.write('\n')
    f.close()
    return [avg_agg_rating], ['East Coast']


def getWestTotalAggregrate(cur, conn):
    cur.execute('SELECT * FROM West_Coast_Rests')
    total = 0
    num_res = 0
    for row in cur:
        total += row[7]
        num_res += 1
    avg_agg_rating = total/num_res
    f = open("CalcFiles.txt", "a")
    f.write("West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating))
    f.write('\n\n')
    f.close()
    return [avg_agg_rating], ['West Coast']


def getWestAggregatesPerRating(cur, conn):
    cur.execute('SELECT * FROM West_Coast_Rests')
    total_45 = 0
    num_45res = 0
    total_40 = 0
    num_40res = 0
    total_35 = 0
    num_35res = 0
    for row in cur:
        if row[2] == 4.5:
            total_45 += row[7]
            num_45res += 1
        elif row[2] == 4.0:
            total_40 += row[7]
            num_40res += 1
        elif row[2] == 3.5:
            total_35 += row[7]
            num_35res += 1
    avg_agg_rating_45 = total_45/num_45res
    avg_agg_rating_40 = total_40/num_40res
    avg_agg_rating_35 = total_35/num_35res
    agg_lst = []
    agg_lst.append(avg_agg_rating_35)
    agg_lst.append(avg_agg_rating_40)
    agg_lst.append(avg_agg_rating_45)
    rating_lst = [3.5, 4.0, 4.5]
    f = open("CalcFiles.txt", "a")
    f.write("4.5 West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_45))
    f.write('\n')
    f.write("4.0 West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_40))
    f.write('\n')
    f.write("3.5 West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_35))
    f.write('\n\n')
    f.close()
    return agg_lst, rating_lst


def getEastAggregatesPerRating(cur, conn):
    cur.execute('SELECT * FROM East_Coast_Rests')
    total_45 = 0
    num_45res = 0
    total_40 = 0
    num_40res = 0
    total_35 = 0
    num_35res = 0
    for row in cur:
        if row[2] == 4.5:
            total_45 += row[7]
            num_45res += 1
        elif row[2] == 4.0:
            total_40 += row[7]
            num_40res += 1
        elif row[2] == 3.5:
            total_35 += row[7]
            num_35res += 1
    avg_agg_rating_45 = total_45/num_45res
    avg_agg_rating_40 = total_40/num_40res
    avg_agg_rating_35 = total_35/num_35res
    agg_lst = []
    agg_lst.append(avg_agg_rating_35)
    agg_lst.append(avg_agg_rating_40)
    agg_lst.append(avg_agg_rating_45)
    rating_lst = [3.5, 4.0, 4.5]
    f = open("CalcFiles.txt", "a")
    f.write("4.5 East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_45))
    f.write('\n')
    f.write("4.0 East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_40))
    f.write('\n')
    f.write("3.5 East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_35))
    f.write('\n\n')
    f.close()
    return agg_lst, rating_lst


def getWestAggregatesPerPrice(cur, conn):
    cur.execute('SELECT * FROM West_Coast_Rests')
    total_triple = 0
    num_tripleres = 0
    total_double = 0
    num_doubleres = 0
    total_single = 0
    num_singleres = 0
    for row in cur:
        if row[1] == '$$$':
            total_triple += row[7]
            num_tripleres += 1
        elif row[1] == '$$':
            total_double += row[7]
            num_doubleres += 1
        elif row[1] == '$':
            total_single += row[7]
            num_singleres += 1
    avg_agg_rating_triple = total_triple/num_tripleres
    avg_agg_rating_double = total_double/num_doubleres
    avg_agg_rating_single = total_single/num_singleres
    agg_lst = []
    agg_lst.append(avg_agg_rating_single)
    agg_lst.append(avg_agg_rating_double)
    agg_lst.append(avg_agg_rating_triple)
    price_lst = ['Low Price','Medium Price','High Price']
    f = open("CalcFiles.txt", "a")
    f.write("$$$ West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_triple))
    f.write('\n')
    f.write("$$ West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_double))
    f.write('\n')
    f.write("$ West Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_single))
    f.write('\n')
    f.close()
    return agg_lst, price_lst


def getEastAggregatesPerPrice(cur, conn):
    cur.execute('SELECT * FROM East_Coast_Rests')
    total_triple = 0
    num_tripleres = 0
    total_double = 0
    num_doubleres = 0
    total_single = 0
    num_singleres = 0
    for row in cur:
        if row[1] == '$$$':
            total_triple += row[7]
            num_tripleres += 1
        elif row[1] == '$$':
            total_double += row[7]
            num_doubleres += 1
        elif row[1] == '$':
            total_single += row[7]
            num_singleres += 1
    avg_agg_rating_triple = total_triple/num_tripleres
    avg_agg_rating_double = total_double/num_doubleres
    avg_agg_rating_single = total_single/num_singleres
    agg_lst = []
    agg_lst.append(avg_agg_rating_single)
    agg_lst.append(avg_agg_rating_double)
    agg_lst.append(avg_agg_rating_triple)
    price_lst = ['Low Price','Medium Price','High Price']
    f = open("CalcFiles.txt", "a")
    f.write("$$$ East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_triple))
    f.write('\n')
    f.write("$$ East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_double))
    f.write('\n')
    f.write("$ East Coast Restaurants have an average aggregate rating of " + str(avg_agg_rating_single))
    f.write('\n\n')
    f.close()
    return agg_lst, price_lst


y1, x1 = getEastTotalAggregrate(cur, conn)
y2, x2 = getWestTotalAggregrate(cur, conn)
y_lst_e1, x_lst_e1 = getEastAggregatesPerRating(cur, conn)
y_lst_w1, x_lst_w1 = getWestAggregatesPerRating(cur, conn)
y_lst_e2, x_lst_e2 = getEastAggregatesPerPrice(cur, conn)
y_lst_w2, x_lst_w2 = getWestAggregatesPerPrice(cur, conn)

#Visualization #1
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax1.plot(x_lst_e1, y_lst_e1, 'b-', label="East Coast")
ax1.plot(x_lst_w1, y_lst_w1, 'r-', label="West Coast")
ax1.legend()
ax1.set(xlabel='Rating', ylabel='Aggregate Rating',
       title='Aggregate Ratings for East and West Coast Cities per Rating')
ax1.grid()

#Visualization #2
ax2 = fig.add_subplot(132)
ax2.plot(x_lst_e2, y_lst_e2, 'o-', label="East Coast")
ax2.plot(x_lst_w2, y_lst_w2, 'x-', label="West Coast")
ax2.set_xlabel('Price')
ax2.set_ylabel('Aggregate Rating')
ax2.set_title('Aggregate Ratings for East and West Coast Cities per Price')
ax2.grid()
ax2.legend()

#Visualization #3
ax3 = fig.add_subplot(133)
ax3.bar([x1[0], x2[0]], [y1[0], y2[0]])
ax3.set_ylabel('Aggregate Rating')
ax3.set_title('Aggregate Ratings for East and West Coast Cities')
ax3.grid()

plt.show()
fig.savefig("Visualizations.png")