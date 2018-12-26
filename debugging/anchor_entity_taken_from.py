# prints the titles of entities that contained the given anchor related to the given entity title
import mysql.connector
import sys

mydb = mysql.connector.connect(host='localhost', user='root', passwd='203761333',database='projectdb')

mycursor = mydb.cursor()

mention  = sys.argv[1]
entity = sys.argv[2]
mention = mention.encode()
mention = mention.decode('utf-8')
entity = entity.encode()
entity = entity.decode('utf-8')


query = 'SELECT Taken_From FROM AnchorTable WHERE Alias =%s AND Title =%s'
val = (mention,entity)
mycursor.execute(query,val)
entities = mycursor.fetchall()

for entity in entities:
    print(entity[0])

