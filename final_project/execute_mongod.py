import signal
import subprocess
from pymongo import MongoClient
import pprint


### Use the subprocess module to run shell commands.
# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
pro = subprocess.Popen("mongod", preexec_fn = os.setsid) 


### Connect database with pymongo
db_name = "osm"
client = MongoClient('localhost:27017')
db = client[db_name]




### This code will build a mongoimport command, then use subprocess.call to execute
# Build mongoimport command
collection = filename[:filename.find(".")]
#print collection
working_directory = "/Users/ducvu/Documents/ud032-master/final_project/"

json_file = filename + ".json"
#print json_file
mongoimport_cmd = "mongoimport --db " + db_name + \
                  " --collection " + collection + \
                  " --file " + working_directory + json_file
#print mongoimport_cmd 

# Before importing, drop collection if it exists
if collection in db.collection_names():
    print "dropping collection"
    db[collection].drop()

# Execute the command
print "Executing: " + mongoimport_cmd
subprocess.call(mongoimport_cmd.split())



if __name__ == "__main__":

    
    #Get the collection from the database
    boston_db = db[collection]

    #Number of Documents
    boston_db.find().count()

    #Number of Unique Users
    len(boston_db.distinct('created.user'))
    
    
    #Number of Nodes and Ways
    node_way = boston_db.aggregate([
        {"$group" : {"_id" : "$type", "count" : {"$sum" : 1}}}])

    pprint.pprint(list(node_way))
    
    
    #Top Contributing User
    top_user = boston_db.aggregate([
    {"$match":{"type":"node"}},
    {"$group":{"_id":"$created.user","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":1}
    ])

    pprint.pprint(list(top_user))
    
    
    #Number of users having only 1 post
    type_buildings = boston_db.aggregate([
    {"$group":{"_id":"$created.user","count":{"$sum":1}}},
    {"$group":{"_id":{"postcount":"$count"},"num_users":{"$sum":1}}},
    {"$project":{"_id":0,"postcount":"$_id.postcount","num_users":1}},
    {"$sort":{"postcount":1}},
    {"$limit":1}
    ])

    pprint.pprint(list(type_buildings))
    
    
    #Zip codes
    zipcodes = boston_db.aggregate([
        {"$match" : {"address.postcode" : {"$exists" : 1}}}, \
        {"$group" : {"_id" : "$address.postcode", "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

    pprint.pprint(list(zipcodes))
    
    
    #Top 5 Most Common Cities
    cities = boston_db.aggregate([{"$match" : {"address.city" : {"$exists" : 1}}}, \
                           {"$group" : {"_id" : "$address.city", "count" : {"$sum" : 1}}}, \
                           {"$sort" : {"count" : -1}}, \
                           {"$limit" : 5}])

    pprint.pprint(list(cities))
    
    
    #Top 10 Amenities
    amenities = boston_db.aggregate([
        {"$match" : {"amenity" : {"$exists" : 1}}}, \
        {"$group" : {"_id" : "$amenity", "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}, \
        {"$limit" : 10}])

    pprint.pprint(list(amenities))
    
    
    #Most common building types
    type_buildings = boston_db.aggregate([
    {'$match': {'building': {'$exists': 1}}}, 
    {'$group': { '_id': '$building','count': {'$sum': 1}}},
    {'$sort': {'count': -1}}, {'$limit': 20}
    ])

    pprint.pprint(list(type_buildings))
    
    
    
    #Top Religions with Denominations
    religions = boston_db.aggregate([
        {"$match" : {"amenity" : "place_of_worship"}}, \
        {"$group" : {"_id" : {"religion" : "$religion", "denomination" : "$denomination"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

    pprint.pprint(list(religions))

        
    #Top 10 Leisures
    leisures = boston_db.aggregate([{"$match" : {"leisure" : {"$exists" : 1}}}, \
                           {"$group" : {"_id" : "$leisure", "count" : {"$sum" : 1}}}, \
                           {"$sort" : {"count" : -1}}, \
                           {"$limit" : 10}])

    pprint.pprint(list(leisures))
        
    
    #Top 15 Universities
    universities = boston_db.aggregate([
        {"$match" : {"amenity" : "university"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}},
        {"$limit":15}
    ])

    pprint.pprint(list(universities))
    
    
    #Top Prisons
    prisons = boston_db.aggregate([
        {"$match" : {"amenity" : "prison"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

    pprint.pprint(list(prisons))
    
    #Most popular cuisines in fast foods
    fast_food = boston_db.aggregate([
    {"$match":{"cuisine":{"$exists":1},"amenity":"fast_food"}},
    {"$group":{"_id":"$cuisine","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
    ])

    pprint.pprint(list(fast_food))
    
    
    
    
    