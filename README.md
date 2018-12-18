# Wikipedia Entity Linking

This project aims to identify and link text fragments of a given hebrew text document that refer to an entity contained in Wikipedia.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Python 3

*Windows:* 

download IDE for python from: [Download Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

*Linux:* 

install python3 with these commands: 

	 sudo apt-get update
	 sudo apt-get install python3.6

2. Python packages

install the following python packages:

* mysql
* nltk
* string
* xml.etree.ElementTree
* re
* csv

3. mysql

*Windows:*

* Download mysql version 5.7.24 from [here](https://dev.mysql.com/downloads/windows/installer/5.7.html)
* For getting started explanation watch this [tutorial](https://www.youtube.com/watch?v=JFF0iU0zMbI&list=WL&index=8&t=0s)

*Linux:* 

For installing mysql server on linux watch this [tutorial](https://www.youtube.com/watch?v=0o0tSaVQfV4)

connect to the server with this command:

	mysql -u root -p

and enter your password

4. Wikipedia Dump

download and decompress from the wikipedia dump version February 01, 2018 the following files:

* hewiki-20180201-pages-articles.xml.bz2

*Windows:* 

download from the [here](https://archive.org/download/hewiki-20180201)

*Linux:* 

download the file using the following command:

	wget https://archive.org/download/hewiki-20180201/file

decompress the file using the following command (Note that this command doesn't preserve the original archive file):

	bzip2 -d file.bz2

## Usage

### Preparing the database

to create a table with all anchor texts from all of wikipedia articles, run:

	python3 anchor_texts.py

### Spotting 

to create a database run:

	python dbcreator.py

to create a .csv that contains for each text fragment in the input text file entities that are candidates for linking, run:

	python3 Spotter.py input_text_name {your_output_file}.csv