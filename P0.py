from os import truncate
from pymongo import MongoClient,DESCENDING,ASCENDING
from pprint import pprint
from QueryExe import queries
import datetime
import re
from QueryPrint import Qprint


client=MongoClient()

db=client['P0']          #db=client.P0




#x=db.list_collection_names()
#c=x[0]
#d=db.get_collection(c)

d=db['restaurants']        #d=db.restaurants

print("Enter 1 to execute User Query","Enter 2 to execute Queries in P0 Exercise",sep='\n')
choice=int(input("Please Enter choice: "))

if choice==1:
    flag=True
    while flag:
        query=input('\nEnter query:\n')
        temp=input('\nPress  Enter to Continue....\n')

        for e in eval(query):
            pprint(e)
        s=int(input("\nEnter 1 to continue...  or 2 to stop: "))
        if s==2:
            flag=False
else:
    flag=True
    while flag:
        i=int(input("Please Enter Query Number: " ))

        print("\n",Qprint(i))
    
        query= queries[i]
        print('The Query to be Executed is:',query,sep='\n')
        temp=input('\nPress  Enter to Continue....\n')

        for e in eval(query):
            pprint(e)
        s=int(input("\nEnter 1 to continue...  or 2 to stop: "))
        if s==2:
            flag=False
