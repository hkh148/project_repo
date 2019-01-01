from nltk import ngrams
import mysql.connector
import string
import sys
import csv
from macros import *

mydb = mysql.connector.connect(host='localhost', user=USER_NAME, passwd=PASSWORD,database='projectdb')
mycursor = mydb.cursor()
exclude = set(string.punctuation)
exclude.remove("'")

abbrev_dict = {"ר'":"רבי","דר'":"דרבי","ור'":"ורבי"}
def open_abbreviation(word):
	if word in abbrev_dict.keys():
		return abbrev_dict[word]
	return word

input_file = open(sys.argv[1],'r',encoding='utf8')
result = open(sys.argv[2],'w',encoding='utf8')
csv_writer = csv.writer(result,dialect='excel',lineterminator='\n')
csv_writer.writerow(['Mention','Start index','End index','Title','Wikipedia link'])
data = input_file.read()
for i in range(1,4):
	grams = ngrams(data.split(), i)
	start_index = 0
	grams_without_dup = list(set(grams))
	for gram in grams_without_dup:
		if i > 1:
			for j in range(2,i+1):
				if gram[j-1] in abbrev_dict.keys() or gram[j-1] in abbrev_dict.items():
					continue;
		list_of_gram = list(gram)
		list_of_gram[0] = open_abbreviation(list_of_gram[0])
		word = ''.join([w + ' ' for w in list_of_gram]).strip()
		word = ''.join(ch for ch in word if ch not in exclude)
		if "''" in word:
			splitted_list = word.split("''")
			word = ''.join(w + '"' for w in splitted_list)
			word = word[:-1]
		if "'" in word:
			splitted_list = word.split("'")
			word = ''.join(w + "''" for w in splitted_list)
			word = word[:-2]
		query = "SELECT * FROM AnchorTable" \
			" WHERE Alias = '" + word + "';"
		mycursor.execute(query)
		entries = mycursor.fetchall()
		for entry in entries:
			tmp_row = [word,start_index,start_index+i-1,entry[1],entry[0]]
			csv_writer.writerow(tmp_row)
		start_index+=1
input_file.close()
result.close()
mydb.disconnect()
