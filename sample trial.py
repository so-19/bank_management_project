#SOURCE CODE FOR BANKING TRANSACTIONS
print("****BANK TRANSACTION****")
import time
import random
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ozs123*")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank1dup")
mycursor.execute("use bank")
#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6),password varchar(10))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date ,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
import random
import time
def otp():
    global otp
    global otpu
    otp=random.randint(10000,99999)
    print("you will receive an OTP on the screen,Type the OTP when asked")
    print("Your ONE TIME PASSWORD IS::::",otp)
    time.sleep(3)
    otpu=int(input('Enter the OTP you received:'))
def createAccount():
    acno=str(input('Enter account number:'))
    name=input("Enter name(limit 35 characters):")
    city=str(input("Enter city name:"))
    password=input("Enter Your password:")
    balance=0
    mn=str(input("Enter mobile no.:"))
    if len(mn)==10:
        otp()
        if otp==otpu:
            print("Your OTP is correct")
            mycursor.execute("select acno from bank_master")
            data=mycursor.fetchall()
            if (acno,) not in data:
                mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"','"+password+"')")
                print("Account is successfully created!!!")
                mydb.commit()
            else:
                print("The account number is already taken")
                print("Please select another account number")
                createAccount()
        else:
            print("You have entered a wrong OTP")
            createAccount()
    else:
        print("You have entered an invalid Mobile Number")
        createAccount()
    print()

while True:
    print("1=Create account")
    ch=int(input("Enter your choice:"))
    if ch==1:
        createAccount()
    else:
        break
