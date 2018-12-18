# Wikipedia Entity Linking

This project aims to identify and link text fragments of a given hebrew text document that refer to an entity contained in Wikipedia.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<<<<<<< HEAD
First, you have to download or clone this repository to your local machine.

The following programs/packages should be downloaded before running the scripts:

1. Python 3
=======
### 1. Python 3
>>>>>>> 89823d58cde35dae1acbb943e617b6ec3ee55bfa

#### *Windows:* 

download python3 latest version from [python official website](https://www.python.org)

#### *Linux:* 

install python3 with these commands: 

	 sudo apt-get update
	 sudo apt-get install python3.6

### 2. Python packages

install the following python packages using pip installer:

* mysql
* nltk

### 3. mysql

#### *Windows:*

* Download mysql version 5.7.24 from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html)
* For getting started explanation watch this [tutorial](https://www.youtube.com/watch?v=JFF0iU0zMbI&list=WL&index=8&t=0s)

#### *Linux:* 

Follow the following steps to install mysql server on your linux machine:
	1.
		sudo apt-get update
	
	2.
		sudo apt-get install mysql-server
		
	3. When asked, choose 203761333 as your root user password. (if you choose otherwise, certain files should be updated - explained later)

connect to the server with this command:

	mysql -u root -p

and enter your password

### 4. Wikipedia Dump

download and decompress from the wikipedia dump version February 01, 2018 the following files:

* hewiki-20180201-pages-articles.xml.bz2

#### *Windows:* 

download from the [here](https://archive.org/download/hewiki-20180201/hewiki-20180201-pages-articles.xml.bz2)

#### *Linux:* 

download the file using the following command:

	wget https://archive.org/download/hewiki-20180201/hewiki-20180201-pages-articles.xml.bz2

decompress the file using the following command (add -k flag to keep the original compressed file):

	bzip2 -d file.bz2

## Usage

### Preparing the database

if you chose a password of your own, the following files should be updated where it says passwd='203761333' to have passwd='your own password':

	1. dbcreator.py
	2. dbdropper.py
	3. anchor_texts.py
	4. spotter.py
	5. acceptance_test.py
	(so all of them!)
	
run the following command to create a database in the root mysql user:

	python dbcreator.py	

after running this script you should be able to connect to mysql server (see instruction above) and run the following command:
	
	SHOW DATABASES;

and see 'projectdb' in the database list shown.

make sure you quit mysql server by typing 'quit' (without quotation marks)

to create a table with all anchor texts from all of wikipedia articles, run:

	python3 anchor_texts.py
	
this should take a while, you can go take around 2.5 hour break.

to make sure that the table exists in the database you can connect again to mysql server and run the following commands:
	
	USE projectdb;
	SHOW TABLES;

and see 'AnchorTable'.

you can also run the following command:
	
	python3 acceptance-test.py > output
	
and then a wild output file would appear in your directory with some data in it.

### Spotting 

to create a .csv that contains for each text fragment in the input text file entities that are candidates for linking, run:

<<<<<<< HEAD
	python3 Spotter.py {your_input_file} {your_output_file}.csv

for the input file provide your desired text to link and for your output file choose a name (if it doesn't exist it will create it for you) with file name extension .csv
=======
	python3 Spotter.py input_text_name {your_output_file}.csv
>>>>>>> 89823d58cde35dae1acbb943e617b6ec3ee55bfa
