# mysql-selfmanaged

Cloud Environment: GCP

Virtual Machine Set Up

Created new VM instance in GCP
- Machine type: E2, e2-medium
- Architecture: x86/64
- Firewalls: HTTP and HTTPS traffic On
- Boot disk image: ubuntu
- All else is default settings

Firewall Configurations: adding port 3306
- Go to Firewall and click Create Firewall Rule
- Direction of traffic: Ingress
- Specified Targets: All instances in the network 
- Source IPv4 ranges: 0.0.0.0/0
- TCP: 3306 
- Priority: 1000

Commands to set up OS image
$ sudo apt-get update
$ sudo apt install mysql-server mysql-client

Making mysql instance available:
sudo mysql
CREATE USER 'fizzah'@'%'IDENTIFIED BY'ahi2022';
GRANT ALL PRIVILEGES ON *.* TO 'fizzah'@'%' WITH GRANT OPTION;
CREATE DATABASE db1

Create database database name;
show databases;
creating tables:
use {database name}
create table table_name(var1 varchar(255), var2 varchar(255));

Back to SSH browser: 
$ sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf 
change bind-address: 0.0.0.0 
$ sudo /etc/init.d/mysql restart

Inserting data into mysql database, used Google Colab 
Variables:
mysql_Hostname, mysql_User, mysql_Password, mysql_Database
Create engine:
db1 = create_engine(connection_string)
Adding pandas dataframe to mysql database
dataframe_name.to_sql('name', con=db1, if_exisits='replace')


<img width="894" alt="mysql_table" src="https://user-images.githubusercontent.com/111600840/208851811-d957155d-7dbc-42b9-bfec-960592ed06f7.png">
