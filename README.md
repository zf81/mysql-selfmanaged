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

Commands to set up OS image <br>
$ sudo apt-get update <br>
$ sudo apt install mysql-server mysql-client <br>

Making mysql instance available: <br>
sudo mysql <br>
CREATE USER 'fizzah'@'%'IDENTIFIED BY'ahi2022'; <br>
GRANT ALL PRIVILEGES ON *.* TO 'fizzah'@'%' WITH GRANT OPTION; <br>
CREATE DATABASE db1 <br>

Create database database name; <br>
show databases; <br>
creating tables: <br>
use {database name} <br>
create table table_name(var1 varchar(255), var2 varchar(255)); <br>

Back to SSH browser: <br>
$ sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf <br>
change bind-address: 0.0.0.0 <br>
$ sudo /etc/init.d/mysql restart <br>

Inserting data into mysql database, used Google Colab <br>
Variables: <br>
mysql_Hostname, mysql_User, mysql_Password, mysql_Database <br>
Create engine: <br>
db1 = create_engine(connection_string) <br>
Adding pandas dataframe to mysql database <br>
dataframe_name.to_sql('name', con=db1, if_exisits='replace') <br>


<img width="894" alt="mysql_table" src="https://user-images.githubusercontent.com/111600840/208851811-d957155d-7dbc-42b9-bfec-960592ed06f7.png">
