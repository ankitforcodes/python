import pymongo

myclient = pymongo.MongoClient("mongodb+srv://ankit:ankit12168#@cluster0-zrq5o.mongodb.net/opinions_v1?retryWrites=true&w=majority")
dblist = myclient.list_database_names()
print(dblist)