# TODO: optimse searching
from Engine import createVectorDB, searchDB

DB = createVectorDB()

searchQuery = input("Enter query: ")

searchDB(searchQuery, DB)
