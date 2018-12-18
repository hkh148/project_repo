import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="203761333",
    database="projectdb"
)

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM AnchorTable")
mycursor.execute("DROP TABLE AnchorTable")
