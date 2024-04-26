# python-flask-mysql
This is just a simple demo how to develop a webservice using python, flask and mysql. ``pymysql`` python mysql driver is used here.

Steps performed:
----------------
Download python3, pip3, gunicode and mysql-server

Update packages:
```
sudo apt-get update
```
Install Python3 and PIP3:
```
sudo apt-get install python3 python3-pip
sudo apt-get install libmysqlclient-dev
```
Verify installation:
```
python3 --version
pip3 --version
```

### Install required python packages

```
   $ pip install -r requirements.txt
```

MYSQL:

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
Credentials of new user:
username: satya
password: Shiva@1192

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
### Config and start webservice

##### Configure MySQL settings

In ``config.py`` file, fill in your real MySQL connection settings

```
_DB_CONF = {
 'host':'localhost',
 'port':3306,
 'user':'satya',
 'passwd':'Shiva@1192',
 'db':'student'
}
```

We are placing the host as "localhost" as the application and MySql database is hosted on Ubuntu EC2.

Start web service:
```
gunicorn -b :8080 main:app
```
Make sure you run this line in the directory that has main.py file.

Test your webservice using curl

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

You should be able to see the website with a table:
![image](https://github.com/satyamounika11/democrudapp/assets/37068004/d07d3cf8-c50f-4d1a-ade7-7058f2dc4e95)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Implementing it with RDS:
Create aws RDS instance and create a database there, instead of MySQL server inside EC2 use this sql file to upload data later.:

AWS --> RDS --> Create database --> Standard create --> MySQL --> Free Tier --> username : admin --> Password: Tosvert123# --> DB instance type: db.t3.micro --> Storage : 20GB General Purpose SSD --> Dont connect to EC2 --> Default VPC --> Security Groups : launch-wizard-1 --> database name : student --> Port: 3306 --> No backup --> Create database 

Launch instance:
EC2 --> Name: rds-student --> Ubuntu --> t2.micro --> key: devops.pem --> VPC: default --> Security Group : launch-wizard-1 --> Launch instance

Login to EC2:
```
sudo apt update
```
Install python3, pip3 and gunicorn:
```
sudo apt install python3 python3-pip
sudo apt install gunicorn
```
Check versions:
```
python3 --version
pip3 --version
```
Installation of MYSQL-Server in EC2 Ubuntu:
```
sudo apt install mysql-server
```
Version:
```
mysqld --version
```
Start SQL service:
```
sudo systemctl start MySQL
```

Check status of MYSQL:
```
sudo systemctl status mysql
```

Clone the repository that has SQL file in it:
```
git clone https://github.com/satyamounika11/democrudapp.git
ls
cd democrudapp
ls
```
(make sure the sql file is present in this path)
```
pip install -r requirements.txt
```
Make sure the config.py is updated with the hostname = rds endpoint, username and password that has been created while creating the RDS DB.

```
import os

_DB_CONF = {
 'host': os.getenv('DB_HOST', 'student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com'),
 'port': int(os.getenv('DB_PORT', 3306)),
 'user': os.getenv('DB_USER', 'admin'),
 'passwd': os.getenv('DB_PASSWORD', 'Tosvert123#'),
 'db': os.getenv('DB_NAME', 'student')
}
```

Login to RDS Database using the endpoint and username that has been created while creating the RDS DB :
```
mysql -h student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com -u admin -p
```
Create a database:
```
CREATE DATABASE student;
```
Create User:
```
CREATE USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Tosvert123#';
```
Grant privileges:
```
GRANT ALL PRIVILEGES ON student.* TO 'admin'@'localhost';
```
To make sure the privileges take effect:
```
FLUSH PRIVILEGES;
```
Exit SQL:
```
Exit;
```
Restart the SQL:
```
sudo systemctl restart MySQL
```

Import your SQL dump file:
```
mysql -h student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com -u admin -p student < student_persons.sql
```
(student_persons.sql file should be present in the same directory where you are running these commands)

Login to MySQL:
```
mysql -h student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com -u admin -p

USE student;
SHOW TABLES;
SELECT * FROM persons;
```
(Displays the content in table)

Make sure port 3306 is opne in secuirty groups.

Exit SQL:
```
Exit;
```
Start webservice:
```
gunicorn -b :8080 main:app
```

Open the url in browser:
```
http://<SERVER-IP>:8080
```
(Optional: Also, a new file gunicorn_pid.text file will be generated that has the PID of the SQL that's hosting, if you run main.py.)

EG:
```
cat gunicorn_pid.txt
4877
```

Now, create an ALB for this application.

Got to AWS --> Route53 --> Hosted zones --> sasidatta.com --> Create record --> mouni.sasidatta.com --> Value: Public-IP-Addresss--> create record.

Create ALB --> Load balancers --> Create LB --> Application Load balancer --> Instances --> name: mouni-sasidatta-alb --> scheme  internet-facing -->IP Address: IPV4 --> Listener: HTTP, Port: 80 --> Create target group --> select instances --> target name: mouni-app-targets --> protocol: HTTP: 8080 --> Register target: Select instance that's running --> Port: 8080 --> Create Load balancer.

After the ALB is created, it will be assigned a DNS name (e.g., mouni-sasidatta-alb-1234567890.region.elb.amazonaws.com).

Go to Route53 --> Go to record "mouni.sasidatta.com" --> Edit record --> Instead of A record, choose CNAME --> Value: provide the ALB DNS name instead of public IP address --> Save record.

Now, run the command : 
Start web service:
```
gunicorn -b :8080 main:app
```

Go to URL:
```
http://mouni.sasidatta.com/
```

![moni](https://github.com/satyamounika11/democrudapp/assets/37068004/914c7535-8ca7-4a13-87be-e91d395bc4d2)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Creating a Docker image of the application and pushing it to ECR:

A Dockerfile has been created for the my-flask-app application. Check the repo for reference.

Install Docker:
```
sudo apt install docker.io
```

First, add your user to Docker group:
```
sudo usermod -aG docker $USER
```

Build the Docker image:
```
docker build -t my-flask-app .
```

Run your Docker Container:
```
docker run -d -p 8099:8099 -e DB_HOST=student.chbcdne9jh1l.ap-south-1.rds.amazonaws.com -e DB_USER=admin -e DB_PASSWORD=Tosvert123# -e DB_NAME=student my-flask-app
```

Open the url in browser:
```
http://ec2-public-ip:8099
```

Push the image to ECR:

Make sure AWS CLI is installed.
```
sudo apt install awscli
```

Configure AWS CLI:
```
aws configure
```
Give your Access key, Secret Key, Region and format

Steps to create a repo:
Go to AWS and create a private repository: my-flask-app-repo.

Now we need to push the Docker image to this repo.

Use the AWS CLI:
```
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin accountid.dkr.ecr.ap-south-1.amazonaws.com
```
(ACCOUNTID should be your AWS AccountID)

Build your Docker image using the following command:
```
docker build -t my-flask-app-repo .
```

After the build completes, tag your image so you can push the image to this repository:
```
docker tag my-flask-app-repo:latest accountid.dkr.ecr.ap-south-1.amazonaws.com/my-flask-app-repo:latest
```

Run the following command to push this image to your newly created AWS repository:
```
docker push 819821926402.dkr.ecr.ap-south-1.amazonaws.com/my-flask-app-repo:latest
```

![image](https://github.com/satyamounika11/democrudapp/assets/37068004/5cb1e018-065b-486b-a4ee-8fafddc517ee)



