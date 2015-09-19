import pymongo
import bottle
import sys

@bottle.get("/hw1/<n>")

def get_hw1(n):
    connection = pymongo.MongoClient("mongodb://localhost")

    n = int(n)

    db = connection.m101
    collection = db.funnynumbers

    magic = 0

    try:
        iter = collection.find({},limit=1, skip=n).sort('value', direction=1)
        for item in iter:
            return str(int(item['value'])) + "\n"
except:
    print "Error trying to read collection:", sys.exc_info()[0]


bottle.debug(True)
bottle.run(host='localhost', port=8080)

