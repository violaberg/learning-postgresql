import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 1 - select "Name" column from "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 1 - select only "Queen" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 1 - select only by "ArtistId" #51 from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 1 - select only by "ArtistId" #51 from "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 1 - select only by "Composer" from "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results(multiple)
results = cursor.fetchall()

# fetch the result(single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)