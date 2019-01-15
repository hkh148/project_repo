import xml.etree.ElementTree as ET
import re
import mysql.connector
from langdetect import detect
import time
mydb = mysql.connector.connect(host='localhost', user='root', passwd='203761333',database='mydatabase')

mycursor = mydb.cursor()
start = time.time()
mycursor.execute("CREATE TABLE IF NOT EXISTS AnchorTable (Link VARCHAR(700) NOT NULL, Title VARCHAR(255) NOT NULL, Alias VARCHAR(255) NOT NULL, PRIMARY KEY (Title, Alias) )")

lines = []
anchors_lst = []
anchors = []
i = 0
j = 0
taken_from = ''
for event, elem in ET.iterparse('hewiki-20180201-pages-articles.xml', events=("start", "end")):
    if event == 'end' and elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}title':
        taken_from = elem.text
        taken_from = taken_from.encode()
        taken_from = taken_from.decode('utf-8')
    if event == 'end'and elem.tag =='{http://www.mediawiki.org/xml/export-0.10/}text':
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
            try:
                lang = detect(page_name)
                if lang != 'he':
                    print('oops this is i ', i)
                    i = i + 1
                    continue
            except:
                print('oops', j, page_name)
                continue
            j = j + 1
            if j > 1000:
                break
            anchor_text = anchor_text.encode()
            anchor_text = anchor_text.decode('utf-8')
            link = 'https://he.wikipedia.org/wiki/' + str(page_name)
            anchors += [page_name, anchor_text, str(taken_from)]
            #print('link: ' + link + ' ,' + ' page name: ' + page_name + ',' + ' anchor text: ' + anchor_text + ',' + ' taken from: ' + taken_from)
            # mycursor.fetchall()
            query_insert = 'INSERT IGNORE INTO AnchorTable (Link, Title, Alias) VALUES (%s, %s, %s)'
            val_insert = (link, page_name, anchor_text)
            mycursor.execute(query_insert, val_insert)
        anchors_lst = []
        lines = []
mydb.commit()
mydb.disconnect()
print('elapses ', time.time() - start)


