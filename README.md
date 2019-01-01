# Wikipedia Entity Linking

This project aims to identify and link text fragments of a given hebrew text document that refer to an entity contained in Wikipedia.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

First, you have to download or clone this repository to your local machine, check [this link](https://help.github.com/articles/cloning-a-repository/#platform-linux) for explanation.

The following programs/packages should be downloaded before running the scripts:


### 1. Python 3

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

#### *Linux:* 

install a package using the following command:

	python -m pip install SomePackage

### 3. mysql

#### *Windows:*

* Download mysql version 5.7.24 from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html)
* For getting started explanation watch this [tutorial](https://www.youtube.com/watch?v=JFF0iU0zMbI&list=WL&index=8&t=0s)

#### *Linux:* 

Follow the following steps to install mysql server on your linux machine:
	
	sudo apt-get update
	sudo apt-get install mysql-server
		
When asked, choose 203761333 as your root user password. (if you choose otherwise, certain files should be updated - explained later)

to connect to the server you can use this command:

	mysql -u root -p

and enter your password, and then go wild with it but make sure to exit the database by typing 'quit' (without quotation marks)

### 4. Wikipedia Dump

download and decompress from the wikipedia dump version February 01, 2018 the following files:

* hewiki-20180201-pages-articles.xml.bz2

#### *Windows:* 

download from link [here](https://archive.org/download/hewiki-20180201/hewiki-20180201-pages-articles.xml.bz2) to the same directory you downloaded the repo

#### *Linux:* 

download the file using the following command from within the directory containing the repo:

	wget https://archive.org/download/hewiki-20180201/hewiki-20180201-pages-articles.xml.bz2

decompress the file using the following command (add -k flag to keep the original compressed file):

	bzip2 -d file.bz2

## Usage

### Preparing the database

if you chose a password of your own	you should update the file 'macros.py' to have your own user name (typically it should stay root unless you change it) and your own password in the corresponding variables

dbutils.py is provided as a tool to create, clear and delete a database, before the next steps you should create the database using said file by typing:
    
    python3 dbutils create

after running the command you should see 'projectdb' in the output.

to fill a table with all anchor texts from all of wikipedia articles, run:

	python3 anchor_texts.py &
	
this should take a while, you can go take around 2.5 hour break.

to make sure that the table exists in the database you can connect again to mysql server and run the following commands:
	
	USE projectdb;
	SHOW TABLES;

and see 'AnchorTable'.

or alternatively, you can type the following command (while still logged to mysql server) and see an actual content:
    
    SELECT * FROM AnchorTable LIMIT 10;

this shows the first 10 rows that exist in the table.

### Spotting 

to create a .csv that contains for each text fragment in the input text file entities that are candidates for linking, run:

	python3 Spotter.py {your_input_file} {your_output_file}.csv &

for the input file provide your desired text to link and for your output file choose a name (if it doesn't exist it will create it for you) with file name extension .csv

