TODO = "Optimime case sesitive search"
# TODO: optimse searching
from Engine import createVectorDB, searchDB

DB = createVectorDB()

searchQuery = input("Enter query: ")

results = searchDB(searchQuery, DB)
