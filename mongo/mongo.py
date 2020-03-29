from pymongo import MongoClient
from pprint import pprint

dbh = MongoClient('localhost:27017')
dbo = dbh.business
serverStatusResult = dbo.command("serverStatus")
pprint(serverStatusResult)

