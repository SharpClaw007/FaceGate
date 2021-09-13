from pymongo import MongoClient
import pymongo
from pprint import pprint
import certifi

i=0

ca = certifi.where()

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://SharpClaw007:jcrc8383@cluster0.n5s2p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)

    # Create the database for our example (we will use the same database throughout the tutorial
studentlist = client['studentlist']

col = studentlist['Students']

def testcall():
    try:
        #pprint(col.find_one())
        for x in col.find():
            pprint(x)
    except:
        print('No response, trying again.', i)
        testcall()
        i+1

#name = str(input('What is the name of the student?'))
#status = bool(input())

#push1 = { 'Name' : name, 'Present' : status}
delete1 = {'Name' : 'Student B'}

#x = col.insert_one(push1)
col.delete_one(delete1)

testcall()