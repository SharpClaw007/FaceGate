from pymongo import MongoClient
import pymongo
from pprint import pprint
import certifi

ca = certifi.where()

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://SharpClaw007:jcrc8383@cluster0.n5s2p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)

    # Create the database for our example (we will use the same database throughout the tutorial
studentlist = client['studentlist']

col = studentlist['Students']

def start():
    print('This program will check in or out students based on an ID input.\nPlease enter the ID below:\n')
    id_input = int(input())
    myquery = {'ID' : id_input}
    cur = col.find({'ID': id_input})

    if cur.count()==0:
        print('No students found in search.')
    else:
        for x in col.find({'ID': id_input}):
            print('\n')
            pprint(x)
        print('\nAre you checking the student in or out?\n(True for in, False for out)\n')
        newstatus = input()
        if newstatus == 'True':
            newstatusreal = True
        elif newstatus == 'False':
            newstatusreal = False
        else:
            print('Please enter a valid response.')
        newvalues = {'$set': {'Present': newstatusreal}}
        col.update_one(myquery, newvalues)
        print('\nUpdate complete.')
    
    
start()    