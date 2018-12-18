import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="203761333"
)

cursor = mydb.cursor()
cursor.execute("CREATE SCHEMA projectdb DEFAULT CHARACTER SET utf8")

cursor.execute("SHOW DATABASES")
for x in cursor:
	print(x)


