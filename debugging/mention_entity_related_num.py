# prints number of times the given mention and the given entity are related in wikipedia
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


query = 'SELECT COUNT(*) FROM AnchorTable WHERE Alias =%s AND Title =%s'
val = (mention,entity)
mycursor.execute(query,val)
result = mycursor.fetchone()

print(result[0])

