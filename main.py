#This database has many tables. Write an SQL command that will print Name from the table Artist (for all the database entries)
#Print all data from the table Invoice where BillingCountry is Germany
#Count how many albums are in the database. Look into the SQL documentation for help. Hint: look for Min&Max and Count, Avg, Sum.
#How many customers are from France?

from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")


#TASK 1
db.execute("SELECT Name FROM Artist;")

result = db.execute("SELECT Name FROM Artist;")

db.pretty_print("SELECT Name FROM Artist;")


#TASK 2
db.execute("SELECT * FROM Invoice WHERE Invoice.BillingCountry = 'Germany';")

db.pretty_print("SELECT * FROM Invoice WHERE Invoice.BillingCountry = 'Germany';")


#TASK 3
db.execute("SELECT COUNT(*) FROM Album;")
db.pretty_print("SELECT COUNT(*) FROM Album;")


#TASK 4

db.execute("SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France';")
db.pretty_print("SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France';")