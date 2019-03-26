import xml.etree.ElementTree as ET
import mysql.connector
import re
from numpy import double
import time

mydb = mysql.connector.connect(host='localhost', user='root', passwd='203761333',database='mydb')
# mydb = mysql.connector.connect(host='localhost', user='hadeel', passwd='pI314159@pi',database='wiki')
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS LinkProbability (Alias VARCHAR(500) NOT NULL, PagesNumAsAnchor INT, PagesNumAsText INT, LP DOUBLE, PRIMARY KEY (Alias) )")

print('started fetching all anchors at: ', time.asctime( time.localtime(time.time()) ))
# getting all anchors
query = "SELECT Alias FROM no_dup_anchors;"
mycursor.execute(query)
all_anchors_lst = mycursor.fetchall()

print('started getting all relevant pages at: ', time.asctime( time.localtime(time.time()) ))
# getting all relevant pages
query = "SELECT DISTINCT IncludingTitle FROM relevant_anchor_table;"
mycursor.execute(query)
all_pages_titles_lst = mycursor.fetchall()
for res in all_pages_titles_lst:
    res = res[0]

print('started calculating anchors as text at: ', time.asctime( time.localtime(time.time()) ))
still_running = 1
anchors_freq_as_text_dict = {}
pattern = ': |, | \(\[\[|\]\]\)| \(\[\[|\]\]\).| \(|\) |-\[\[| \[\[|\]\] | \[|\] |-|\.|; | '

for event, elem in ET.iterparse('hewiki-20180201-pages-articles.xml', events=("start", "end")):
# for event, elem in ET.iterparse('pages-articles-temp.xml', events=("start", "end")):
    if event == 'end' and elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}title':
        page_title = str(elem.text)
        page_title = page_title.encode()
        page_title = page_title.decode('utf-8')
        if page_title not in all_pages_titles_lst:
            continue
    if event == 'end'and elem.tag =='{http://www.mediawiki.org/xml/export-0.10/}text':
        text_words = re.split(pattern, str(elem.text))
        for a in all_anchors_lst:
            anchor = str(a[0])
            if anchor in text_words:
                if str(anchor) not in anchors_freq_as_text_dict:
                # first time that I want to count this anchor
                    anchors_freq_as_text_dict[str(anchor)] = 1
                else:
                    anchors_freq_as_text_dict[str(anchor)] += 1
        elem.clear()
        text_words = []
    elem.clear()
    if still_running % 1000 == 0:
        print('I\'M STILL RUNNING! at: ', time.asctime(time.localtime(time.time())))
    still_running += 1

print('started calulating anchors mentions as anchors at: ', time.asctime( time.localtime(time.time()) ))

query = "SELECT Alias, COUNT(IncludingTitle) FROM relevant_anchor_table GROUP BY Alias;"
mycursor.execute(query)
anchors_freq_as_anchor_lst = mycursor.fetchall()

print('started filling LP table at: ', time.asctime( time.localtime(time.time()) ))

for r in anchors_freq_as_anchor_lst:
    anchor = r[0]
    pages_num_as_anchor = r[1]
    if anchor in anchors_freq_as_text_dict:
        pages_num_as_text = anchors_freq_as_text_dict[anchor]
        LP = double(int(pages_num_as_anchor) / int(pages_num_as_text))
    else:
        LP = 0
    query_insert = "INSERT IGNORE INTO LinkProbability (Alias, PagesNumAsAnchor, PagesNumAsText, LP) VALUES (%s, %s, %s, %s)"
    val_insert = (anchor, pages_num_as_anchor, pages_num_as_text, str(LP))
    mycursor.execute(query_insert, val_insert)
    mydb.commit()

print('finished at: ', time.asctime( time.localtime(time.time()) ))
mydb.disconnect