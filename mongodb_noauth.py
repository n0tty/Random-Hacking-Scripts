#!/usr/bin/python


#Greetz
def greet():
  print \
  """
  MongoDB Connector and database names extractor using Python v2.7 by n0tty\n
  legendtanoybose@gmail.com
  https://github.com/n0tty

__________
\\______   \\ ____  ______ ____
 |    |  _//  _ \\/  ___// __ \\
 |    |   (  <_> )___ \\\\  ___/
 |______  /\\____/____  >\\___  >
        \\/           \\/     \\/
  """


greet()


#Module start
import pymongo
import time

print \
"""

Reason:
I built this because of unavailability of internet to download the 155+ MB of MongoDB client
on a linux system to generate a PoC during a PenTest

FYI:
This code has not been tested and probably would not work in Python 3.0+
This code has been tried and tested on Kali Linux 1.10 and Python version 2.7.3

"""


ip_address=raw_input("Please enter the IP address of the server: ")


try:
        port=input("Please input the port number (default is 27017): ")
        if (port<=1 or port>=65535):
                port=27017
                print "You have entered an invalid port number and hence default port (27017) has been selected"
except SyntaxError:
        print "You have entered an invalid port number and hence default port (27017) has been selected"
        port=27017

databases=[]

try:
        print "Connecting..."
        conn = pymongo.Connection(ip_address,port)
        print "[+] Connection is Successful"
        time.sleep(2)
        print "[*] Extracting Database Names"
        try:
                databases = conn.database_names()
                print "[+] Got Database Names successfully"
                time.sleep(2)
                print "[*] Dumping database names: "
                for x in range(0,len(databases)):
                        print databases[x]
                        time.sleep(1)
        except pymongo.errors,f:
                        print "Fail to extract databases: %s" % f
except pymongo.errors.ConnectionFailure,e:
        print "Failed to connect to the database: %s" % e

conn.close()


