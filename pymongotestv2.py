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

def addstudent():
    print('How many students would you like to add?\n')
    runtime = int(input())

    for x in range(runtime):
        name = str(input('What is the name of student', x, '?'))
        id_number = int(input('What is the ID of the student? '))
        print('Are they present? (True or False)\n')
        status = input()
        if status == 'True':
            statusreal = True
        elif status == 'False':
            statusreal = False
        else:
            print('Please enter a valid response.')
            break
        push1 = {'ID': id_number, 'Name' : name, 'Present' : statusreal}
        x = col.insert_one(push1)

def removestudent():
    print('Which student would you like to remove?\n')
    name = str(input('What is the name of the student? '))
    delete1 = {'Name' : name}
    col.delete_one(delete1)
    print('Student deleted.')

def modstudent():
    name = str(input('What is the name of the student you would like to modify? '))
    k = str(input('Would you like to modify the name, status, or ID?\n (NAME, STATUS, ID)\n'))
    if k == 'NAME':
        newname = str(input('What is the new name?\n'))
        myquery = {'Name' : name}
        newvalues = {'$set': {'Name': newname}}
        col.update_one(myquery, newvalues)
        print('The update to', name, 'was completed succesfully.')
    elif k == 'STATUS':
        print('Are they present? (True or False)\n')
        #newstatus = bool(input())
        newstatus = input()
        if newstatus == 'True':
            newstatusreal = True
        elif newstatus == 'False':
            newstatusreal = False
        else:
            print('Please enter a valid response.')
        myquery = {'Name': name}
        newvalues = {'$set': {'Present': newstatusreal}}
        col.update_one(myquery, newvalues)
        print('The update to', name, 'was completed successfuly.' )
    elif k == 'ID':
        print('What is the new ID number?\n')
        newid = int(input())
        myquery = {'Name': name}
        newvalues = {'$set': {'ID': newid}}
        col.update_one(myquery, newvalues)
        print('The update to', name, 'was succesful.')

def start():
    u = str(input('Would you like to Add a student, Remove a student, or modify a student?\n(ADD, REMOVE, MOD)\n'))
    if u == 'ADD':
        addstudent()
    elif u == 'REMOVE':
        removestudent()
    elif u == 'MOD':
        modstudent()
    else:
        print('Please enter a valid response.\n')
        start()

start()

for x in col.find():
    print(x)   


