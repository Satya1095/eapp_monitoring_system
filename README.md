# eapp_monitoring_system
project
PREREQUISITES:
    
1.1) Make sure that python is installed. Type the following in the terminal:
	python3 -V (version3) / python -V (other)

It will return the python version. If python is not present, download it from https://www.python.org/downloads/.

1.2) Make sure that MySQL is running. To check the mysql version, type the following in terminal:
	mysql -V
It will return the mysql version. If MySQL is not present, download it from https://dev.mysql.com/downloads/mysql/.


2)   FLASK INSTALLATION:

2.1) First install virtual environment:
	sudo pip3 install virtualenv (version3) / sudo pip install virtualenv (other)

2.2) Open the path, where you want to create your flask directory:
	cd /path/app

2.3) Create a directory to store all the libraries:
	virtualenv hello_flask

2.4) Activate the virtualenv:
	source bin/activate

2.5) Install Flask:
	pip3 install flask (for python version3) / pip install flask (earlier versions)
 

3)   MySQL SCHEMA:

In order to create mysql tables, you need to establish a connection using terminal.

3.1) Run the following command to establish a mysql connection:
	/usr/local/mysql/bin/mysql -uroot -p ( root is the user here)

3.2) It will ask for your password. The user and password credentials are obtained during the installation of MySQL. Once you enter password, connection is established.

3.3) Using the mysql schema, you can create tables. Once you create tables, you can add data into the table by using insert statement.

	INSERT INTO table_name (column_1, column_2, ……) VALUES (value_1, value_2, ….);


4) RUNNING APPLICATION:

I have run my python main file (app.py here) using python IDLE. You can download it from https://www.python.org/downloads/. 
Open the app.py using IDLE and run (fn + F5). You can see the application running in the localhost (http://127.0.0.1:5000).

5) MODULE ERRORS:

If you get “cannot find module errors”, you can install the modules using the following commands in the terminal.

	pip3 install [module_name] (E.g. pip3 install mysql-connector)


