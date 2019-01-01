import xml.etree.ElementTree as ET
import re
import mysql.connector
from macros import *

mydb = mysql.connector.connect(host='localhost', user=USER_NAME, passwd=PASSWORD,database='projectdb')
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS AnchorTable (Id INT AUTO_INCREMENT PRIMARY KEY, Link VARCHAR(2083) NOT NULL, Title VARCHAR(255) NOT NULL, Alias VARCHAR(255) NOT NULL, Taken_From VARCHAR(255) NOT NULL )")

lines = []
anchors_lst = []
anchors = []
he_word = '{{פירושונים|'
he_word = he_word.encode()
he_word = he_word.decode('utf-8')
taken_from = ''

for event, elem in ET.iterparse('hewiki-20180201-pages-articles.xml', events=("start", "end")):
    if event == 'end' and elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}title':
        taken_from = elem.text
        taken_from = taken_from.encode()
        taken_from = taken_from.decode('utf-8')
    if event == 'end'and elem.tag =='{http://www.mediawiki.org/xml/export-0.10/}text':
        # irrelevant pages
        if (he_word in str(elem.text)):
            continue
        word = '[0-9\u0590-\u05fe-\(\)\s]*'
        pattern = re.compile('\[\[' + word + '\'{0,2}' + word + '\|' + word + '\'{0,2}' + word + '\]\]' + '|' + '\[\[' + word + '\]\]')
        anchors_lst = pattern.findall(str(elem.text))
        for a in anchors_lst:
            page_name, anchor_text = '', ''
            if '|' in a:
                first, second = str(a).split('|')
                page_name = first[2:]
                anchor_text = second[:-2]
            else:
                page_name = a[2:-2]
                anchor_text = page_name
            page_name = page_name.encode()
            page_name = page_name.decode('utf-8')
            anchor_text = anchor_text.encode()
            anchor_text = anchor_text.decode('utf-8')

            link = 'https://he.wikipedia.org/wiki/' + str(page_name)

            anchors += [page_name, anchor_text, str(taken_from)]
            # print('link: ' + link + ' ,' + ' page name: ' + page_name + ',' + ' anchor text: ' + anchor_text + ',' + ' taken from: ' + taken_from)
            # mycursor.fetchall()
            query_insert = 'INSERT INTO AnchorTable (Link, Title, Alias, Taken_From) VALUES (%s, %s, %s, %s)'
            val_insert = (link, page_name, anchor_text, taken_from)
            mycursor.execute(query_insert, val_insert)
        anchors_lst = []
        lines = []
mydb.commit()
mydb.disconnect()

