# prints all titles of entities related to a given mention
import mysql.connector
import sys

mydb = mysql.connector.connect(host='localhost', user='root', passwd='203761333',database='projectdb')

mycursor = mydb.cursor()

mention  = sys.argv[1]
mention = mention.encode()
mention = mention.decode('utf-8')

query = "SELECT * FROM AnchorTable" \
			" WHERE Alias = '" + mention + "';"
mycursor.execute(query)
anchors = mycursor.fetchall()

for anchor in anchors:
    print('link to entity: ' + anchor[0] + ', entity title: ' + anchor[1])

