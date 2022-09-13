import mysql.connector as MySQLdb
from time import sleep
from sys import exit
t=str(input("Enter MySQL Password: "))

def tp(text):
    for character in text:
        sleep(0.1)
        print(character, end='', flush=True)
    print()

try:
    db = MySQLdb.connect(host="localhost",user="root",passwd=t)
except:
    tp("\nConnection Failed...\nClosing...\n")

db = MySQLdb.connect(host="localhost",user="root",passwd=t)
cur = db.cursor()

tp("\n-- Successfully Connected to Server --\n")
def create_memtbl():
    #Creating Members table
    cur.execute("create table members(membership_id integer(4) Primary Key, First_name varchar(20) not null, Last_name varchar(20) not null, phone_no char(10) not null unique, Email_ID varchar(35) not null, Points integer default 0);")
    db.commit()
    tp("\nMembers' table created...")
    # Test data For Members
    cur.execute("insert into members values (1001,'Ashok','Ram',9063289666,'ashokram@gmail.com',100), (1002,'Suresh','Dudala',9347801232,'suresh.12254@gmail.com',100), (1003,'Nithish','Kalyan',8142102378,'kalyansmart0033@gmail.com',100), (1004,'Harishwar','Reddy',8688256415,'harishwar.tene@gmail.com',100), (1005,'Hanith','Thummalapalli',9756841262,'hanith.t@gmail.com',100), (1006,'Sarath','Chandra',9290132202,'lsarathchandra@gmail.com',200), (1007,'Vineeth',' Vyas',9182074677,'psaivineethvyas@gmail.com',200), (1008,'Venky','Royal',9542162387,'venk23@gmail.com',200), (1009,'Kalyan','Lucky',6303703873,'kalyanlucky@gmail.com',200), (1010,'Bade','Anil',9645327185,'badeanil@gmail.com',300);")
    db.commit()
    tp("10 test records inserted to Members' table...")
    
def create_roomstbl():
    #Creating Rooms Table
    cur.execute("create table rooms(Room_no char(3) Primary Key,Fee_per_day integer default 1000,Occupancy enum('Occupied','Vacant'),membership_id integer(5) ,Check_in_date date );")
    db.commit()
    tp("\nRooms table created...")
    # Test data For Rooms
    cur.execute("insert into rooms(Room_no,Fee_per_day,Occupancy,membership_id,check_in_date) values ('100',5000,'Occupied',1001,'2022-02-01'), ('101',5000,'Occupied',1002,'2022-02-06'), ('102',7000,'Occupied',1003,'2022-03-01'), ('103',6000,'Occupied',1004,'2022-03-04'), ('104',7000,'Occupied',1005,'2022-03-10'), ('105',6000,'Occupied',1006,'2022-01-31'), ('106',5000,'Occupied',1007,'2022-02-25'), ('107',6000,'Occupied',1008,'2022-02-14'), ('108',7000,'Vacant',NULL,NULL), ('109',6000,'Vacant' ,NULL, NULL);")
    db.commit()
    tp("10 test records inserted to Rooms' table...")

def create_billstbl():
    #Creating Bills Table
    cur.execute("CREATE TABLE Bills(Bill_no integer(5) ZEROFILL, Room_no char(3), Mem_ID integer(4),Days integer, Amount integer, PRIMARY KEY (Bill_no), FOREIGN KEY (Room_no) REFERENCES Rooms(Room_no), FOREIGN KEY (Mem_ID) REFERENCES Members(Membership_ID));")
    print("\nBill's table created...")
    #Test Data For Bills
    cur.execute("insert into bills values(1001,101,1001,10,50000),(1002,109,1001,2,12000),(1003,104,1006,4,28000)")
    db.commit()
    print("3 test records insert to Bills' table...")

def create_db():
    #Creating Database
    cur.execute("create database hotel_management_system")
    db.commit()
    tp("\nDatabase created...")
    cur.execute("use hotel_management_system")

cur.execute("Show databases")
a=cur.fetchall()
if ('hotel_management_system',) in a:
    tp("\nDatabase already exists...")
    cur.execute("Use hotel_management_system")
    cur.execute("show tables")
    b=cur.fetchall()
    if ('members',) in b:
        tp("\nMembers' Table already exists...")
    else:
        create_memtbl()
    if ('rooms',) in b:
        tp("\nRooms Table already exists...")
    else:
        create_roomstbl()
    if ('bills',) in b:
        tp("\nBills Table already exists...")
    else:
        create_billstbl()
else:
    create_db()
    create_memtbl()
    create_roomstbl()
    create_billstbl()
tp("\n-- Setup was Successful --\n")
#Cleaning Environment
db.close()
