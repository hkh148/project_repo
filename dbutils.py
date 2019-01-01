import mysql.connector
import argparse

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="203761333"
)


def dbcreator():
	cursor = mydb.cursor()
	cursor.execute("CREATE SCHEMA projectdb DEFAULT CHARACTER SET utf8")

	cursor.execute("SHOW DATABASES")
	for x in cursor:
		print(x)

def dbclearer():
	mycursor = mydb.cursor()
	mycursor.execute("USE projectdb")
	mycursor.execute("DELETE FROM AnchorTable")
	mycursor.execute("DROP TABLE AnchorTable")

def dbdropper():
	cursor = mydb.cursor()
	cursor.execute("DROP DATABASE projectdb")
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("operation", help="operation",choices=["create","clear","drop"])
	args = parser.parse_args()
	operation = args.operation
	if operation == "create":
		dbcreator()
	if operation == "clear":
		dbclearer()
	if operation == "drop":
		dbdropper()
	mydb.commit()
	mydb.disconnect()
	