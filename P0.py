from os import truncate
from pymongo import MongoClient,DESCENDING,ASCENDING
from pprint import pprint
from QueryExe import queries
import datetime
import re
from QueryPrint import Qprint

""" Making a Connection with MongoClient """
client=MongoClient()    # This will connect on the default host and port

""" Getting a Database """
db=client['P0']          

""" Getting a Collection """
d=db['restaurants']       

print("Enter 1 to execute User Query","Enter 2 to execute Queries in P0 Exercise",sep='\n')
choice=int(input("Please Enter choice: "))

flag=True
while flag:

    if choice==1:
    
        query=input('\nEnter query:\n')

    else:
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
