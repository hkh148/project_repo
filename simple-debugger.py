import argparse
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="203761333",
	database='mydatabase'
)
mycursor = mydb.cursor()

def find_all_titles_for_alias(alias,csv_writer)
	csv_writer.writerow(['Alias','Title','Mentioning article'])
	mycursor.execute("SELECT Title,Taken_From FROM AnchorTable WHERE Alias = '" +  alias + "';"
	entries = mycursor.fetchall()
	for entry in entries:
		tmp_row = [alias, entry[0],entry[1]]
		csv_writer.writerow(tmp_row)
	
def find_all_aliases_for_title(title,csv_writer)
	csv_writer.writerow(['Title','Alias','Mentioning article'])
	mycursor.execute("SELECT Alias,Taken_From FROM AnchorTable WHERE Alias = '" +  title + "';"
	entries = mycursor.fetchall()
	for entry in entries:
		tmp_row = [title, entry[0],entry[1]]
		csv_writer.writerow(tmp_row)
	
	

	
if __name__ == "__name__":
	parser = argparse.ArgumentParser(description="Utility tool help debug the database")
	parser.add_argument("output_csv_file",help="your csv output file")
	parser.add_argument("argument",help="either alias or title",choices=["alias","title"])
	parser.add_argument("input_string",help="the string you want to find")
	arguments = parser.parse_args()
	output_file_path = arguments.output_csv_file
	argument = arguments.argument
	input_string = arguments.input_string
	output_file = open(output_file_path,'w',encoding='utf8')
	csv_writer = csv.writer(output_file,dialect='excel',lineterminator='\n')
	if argument == "alias":
		find_all_titles_for_alias(input_string,csv_writer)
	if argument == "title":
		find_all_aliases_for_title(input_string,csv_writer)
	output_file.close()
	mydb.disconnect()
		
	
