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

def editID():
    print('\nWhat ID would you like to change the ID of the student to?\n(IDs must be under 4 number values)')
    newid = int(input())
    if newid > 9999:
        print('Please enter a valid ID.')
    else:
        newvalues = {'$set': {'ID': newid}}
        col.update_one(myquery, newvalues)
        print('Update complete.')

def editusername():
    print('\nWhat would you like to change the username of the student to?\n')
    newuser = input()
    newvalues = {'$set': {'username': newuser}}
    col.update_one(myquery, newvalues)
    print('Update complete.')

def editpassword():
    print('\nWhat would you like to change the password of the student to?\n')
    newpass = input()
    newvalues = {'$set': {'password': newpass}}
    col.update_one(myquery, newvalues)
    print('Update complete.')

def editname():
    print('\nWhat name would you like to rename the student to?\n')
    newname = input()
    newvalues = {'$set': {'name': newname}}
    col.update_one(myquery, newvalues)
    print('Update complete.')

def editgrade():
    print('\nWhat grade would you like to reassign the student to?\n(Please enter a number 9-12)\n')
    newgrade = int(input())
    if newgrade < 9:
        print('Please enter a valid grade.')
        return
    elif newgrade > 12:
        print('Please enter a valid grade.')
        return
    else:
        newvalues = {'$set': {'grade': newgrade}}
        col.update_one(myquery, newvalues)
        print('Update complete.')

def editstatus():
    print('\nAre you checking the student in or out?\n(True for in, False for out)\n')
    newstatus = input()
    if newstatus == 'True':
            newstatusreal = True
    elif newstatus == 'False':
            newstatusreal = False
    else:
        print('Please enter a valid response.')
    newvalues = {'$set': {'status': newstatusreal}}
    col.update_one(myquery, newvalues)
    print('\nUpdate complete.')


def create():
    print('How many students would you like to add?\n')
    runtime = int(input())

    #ID
    #username
    #password
    #name
    #grade
    #status

    for x in range(runtime): 
        print('What is the ID of the new student?')
        newid = int(input())

        print('What is the username of the new student?')
        newuser = input()

        print('What is the password of the new student?')
        newpass = input()

        print('What is the new name of the student?')
        newname = input()

        print('What is the grade of the new student?')
        newgrade = int(input())

        print('What is the status of the new student?')
        newstatus = str(input())
        if newstatus == 'Present':
            newboolstatus = True
        else:
            newboolstatus = False

        
        push1 = {'ID': newid, 'username' : newuser, 'password' : newpass, 'name' : newname, 'grade' : newgrade, 'status' : newboolstatus}
        col.insert_one(push1)
        print('Student Created.')

def delete():
    print('What is the ID of the student you wish to delete?\n')
    global ident
    global myquery
    ident = int(input())
    myquery = {'ID' : ident}
    col.delete_one(myquery)
    print('Student deleted.')



def start():
    print('Do you want to edit, create, or delete a student?\nCreate\nDelete\nEdit\n')
    y = input()
    if y == 'Create':
        create()
    elif y == 'Delete':
        delete()
    elif y == 'Edit':
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        print('What is the ID of the student you wish to edit?\n')
        global ident
        global myquery
        ident = int(input())
        myquery = {'ID' : ident}
        cur = col.find({'ID': ident})

        if cur.count()==0:
            print('No students found in search.')
        else:
            for x in col.find({'ID': ident}):
                print('\n')
                pprint(x)
                print('\nStudent found. Please enter what field you wish to edit.')
                print('\nID\nUsername\nPassword\nName\nGrade\nStatus\n')
                y = input()
                if y == 'ID':
                    editID()
                elif y == 'Username':
                    editusername()
                elif y == 'Password':
                    editpassword()
                elif y == 'Name':
                    editname()
                elif y == 'Grade':
                    editgrade()
                elif y == 'Status':
                    editstatus()
    else:
        print('Please enter a valid function.')
        return

start()