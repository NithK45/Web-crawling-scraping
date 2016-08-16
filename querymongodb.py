import pymongo
#import fileinput

def get_db():
    from pymongo import MongoClient
    client = MongoClient('ds153735.mlab.com:53735')
    db = client.mongo1db
    db.authenticate('chechi1','chechi1',source='mongo1db')
    return db


#def add_country(db):
 #   db.countries.insert({"name": "Canada"})


def get_data(db):
    str = raw_input ( "Enter the keyword to search : ")
    return db.guardiannews.find({'$text':{'$search':str}})


if __name__ == "__main__":
    db = get_db()
    #add_country(db)
    print
    #get_data(db)
    for data1 in get_data(db):
	print(data1)
