import os
import sqlite3
import json

# REQUIRES: json_data of word data from Merriam Webster API, DB cursor, DB connection
# MODIFIES: .db file
# EFFECTS: Creates tables to store words and their synonyms, extracts 'root words' and their synonyms
#          Inserts words into the database as pairs (root word, synonym)
#          Makes DB insertions in bundles of 20
#          Print statements for each step

def createWordsDBS(json_data, cur, conn):
    print("creating data tables...")
    #drop pre existing tables and create new ones
    cur.execute('DROP TABLE IF EXISTS Positive_Words')
    cur.execute('CREATE TABLE Positive_Words (original_word TEXT, synonym TEXT)')

    cur.execute('DROP TABLE IF EXISTS Negative_Words')
    cur.execute('CREATE TABLE Negative_Words (original_word TEXT, synonym TEXT)')

    #get keys of data in list form
    review_keys = json_data.keys()
    review_keys = list(review_keys)

    pos_root_wrds = json_data['pos_words'].keys()
    neg_root_wrds = json_data['neg_words'].keys()

    #get list of positive words in form of (root word, synonym)
    pst_words = []
    for word_root in pos_root_wrds:
        lst_words = json_data['pos_words'][word_root]
        for synonym in lst_words:
            pst_words.append((word_root, synonym))

    #get list of negative words in form of (root word, synonym)
    neg_words = []
    for word_root in neg_root_wrds:
        lst_words = json_data['neg_words'][word_root]
        for synonym in lst_words:
            neg_words.append((word_root, synonym))

    #store lengths of all negative/positive words
    neg_length = len(neg_words)
    pos_length = len(pst_words)

    # find the minimum length, so database will store the same number of positive and negative words
    # Minimum value also avoids indexing error when writing to database
    if neg_length < pos_length:
        numberInserts = neg_length//20
    else:
        numberInserts = pos_length//20
    print("Performing {} insertions into database for positive and negative words".format(numberInserts))

    # Insert bundles of 20 words ata time using a counter multiplier
    for counter in range(numberInserts):
        for i in range(20):
            idx = i+(20*counter)
            cur.execute('INSERT INTO Positive_Words (original_word, synonym) VALUES (?, ?)',
                (pst_words[idx][0], pst_words[idx][1]))
        for i in range(20):
            cur.execute('INSERT INTO Negative_Words (original_word, synonym) VALUES (?, ?)',
                (neg_words[idx][0], neg_words[idx][1]))

    conn.commit()