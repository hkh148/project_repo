from nltk import ngrams
import mysql.connector
import string
import sys
import csv

mydb = mysql.connector.connect(host='localhost', user='root', passwd='203761333',database='projectdb')
mycursor = mydb.cursor()
exclude = set(string.punctuation)

my_file = open(sys.argv[1],'r',encoding='utf8')
result = open(sys.argv[2],'w',encoding='utf8')
csv_writer = csv.writer(result,dialect='excel',lineterminator='\n')
csv_writer.writerow(['Mention','Start index','End index','Title','Wikipedia link'])
data = my_file.read()
for i in range(1,5):
	grams = ngrams(data.split(), i)
	start_index = 0
	for gram in grams:
		word = ''.join([w + ' ' for w in gram]).strip()
		word = ''.join(ch for ch in word if ch not in exclude)
		if word.find('–') != -1:
			continue
		query = "SELECT * FROM AnchorTable" \
			" WHERE Alias = '" + word + "';"
		mycursor.execute(query)
		entries = mycursor.fetchall()
		for entry in entries:
			tmp_row = [word,start_index,start_index+i-1,entry[1],entry[0]]
			csv_writer.writerow(tmp_row)
		start_index+=1
my_file.close()
result.close()
