# python-flask-mysql
This is just a simple demo how to develop a webservice using python, flask and mysql. ``pymysql`` python mysql driver is used here.

```
$ python -V
Python 3.6.0 
```

### Install required python packages

```
   $ pip install -r requirements.txt
```

### Config and start webservice

##### Configure MySQL settings

In ``config.py`` file, fill in your real MySQL connection settings

```
_DB_CONF = {
 'host':'127.0.0.1',
 'port':3306,
 'user':'lalitha',
 'passwd':'Lalli@2407',
 'db':'student'
}
```

##### Change MySQL query

In ``main.py`` file, put your real mysql select query here

```
    sql="<PUT YOUR MySQL QUERY HERE>"
```


##### Start Webservoce

```
   $ gunicorn -b :8080 main:app
```

### Test your webservice using curl

```
   curl http://localhost:8080/test
```

You can also test your webservice remotely

```
   curl http://<SERVER-IP>:8080/test
```

If you have trouble with 'Access-Control-Allow-Origin' error when making cross-origin ajax call,  add the following

```
from flask_cors import CORS

app = Flask(__name__)

"""
CORS function is to avoid No 'Access-Control-Allow-Origin' error
"""
CORS(app)
```

sudo apt-get install libmysqlclient-dev
sudo apt install python3-pip


--------------------------------------------------
DemoCrudApp:
Download python3, pip3, gunicode and mysql-server

MYSQL:

username: satya
password: Shiva@1192
(steps to create a username and password are given below)

MYSQL version: 8.0.36

Installation of MYSQL-Server in EC2 Ubuntu:
```
sudo apt install mysql-server
```

Version:
mysqld --version

Start SQL service:
```
sudo systemctl start mysql
sudo service mysql start
```

Check the status of MYSQL:
```
sudo systemctl status MySQL
```


Securing MySQL:
```
sudo mysql_secure_installation
```

Asks for Password Validation:
Enter Y and give a value of 0/1/2 of your choice.

Password authentication might get skipped.
Skipping password set for root as authentication with auth_socket is used by default.
If you would like to use password authentication instead, this can be done with the "ALTER_USER" command.
See https://dev.mysql.com/doc/refman/8.0/en/alter-user.html#alter-user-password-management for more information.

From there, you can press Y and then ENTER to accept the defaults for all the subsequent questions. This will remove some anonymous users and the test database, disable remote root logins, and load these new rules so that MySQL immediately respects the changes you have made.

Login to SQL:
```
sudo MySQL
```

Check the current authentication of the root user:
```
SELECT user, authentication_string, plugin FROM mysql.user;
```

Alter the root user:
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Shiva@1192';
FLUSH PRIVILEGES;
```

Create a user:
```
CREATE USER 'satya'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Shiva@1192';
```

Grant privileges:
```
GRANT ALL PRIVILEGES ON student.* TO 'satya'@'localhost';
```

To make the changes take effect and free up some memory:
```
FLUSH PRIVILEGES;
```
Exit SQL:
```
EXIT;
```
Restart SQL:
```
sudo systemctl start MySQL
```

Login:
```
mysql -u satya -p
```
Prompts one to enter the password.

Create a database:
```
CREATE DATABASE student;
```
Exit SQL:
```
Exit;
```

Import your SQL dump file:
```
mysql -u satya -p student < student_persons.sql
```
(student_persons.sql file should be present in the same directory where you are running these commands)


Log in with the user that you have created:
```
mysql -u satya -p
```
Prompts one to enter a password.

Enter the below steps to view the table:
```
USE student;
SHOW TABLES;
SELECT * FROM persons;
```
(Displays the content in table)

Make sure port 3306 is open in security groups.
```
Exit;
```

Start web service:
```
gunicorn -b :8080 main:app
```

Open the URL in the browser:
```
http://<SERVER-IP>:8080/test
```

You should be able to see the website with a table:
![image](https://github.com/satyamounika11/democrudapp/assets/37068004/d07d3cf8-c50f-4d1a-ade7-7058f2dc4e95)


