import pickle
import os
import pathlib
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ozs123*")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bankmanagement")
mycursor.execute("use bankmanagement")
#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date ,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()
def createAccount(self):
    print("All information prompted are mandatory to be filled")
    acno=str(input("Enter account number:"))
    name=input("Enter name(limit 35 characters):")
    city=str(input("Enter city name:"))
    mn=str(input("Enter mobile no.:"))
    balance=0
    mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
    mydb.commit()
    print("Account is successfully created!!!")
          
    
def showAccount(self):
    print("Account Number : ",self.accNo)
    print("Account Holder Name : ", self.name)
    print("Type of Account",self.type)
    print("Balance : ",self.deposit)
    
def modifyAccount(self):
    print("Account Number : ",self.accNo)
    self.name = input("Modify Account Holder Name :")
    self.type = input("Modify type of Account :")
    self.deposit = int(input("Modify Balance :"))
    mycursor.executemycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
    mydb.commit()
        
def depositAmount(self,amount):
    acno=str(input("Enter account number:"))
    dp=int(input("Enter amount to be deposited:"))
    dot=str(input("enter date of transaction:"))
    ttype="d"
    mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
    mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
    mydb.commit()
    print("money has been deposited successully!!!")
    
def withdrawAmount(self,amount):
    acno=str(input("Enter account number:"))
    wd=int(input("Enter amount to be withdrawn:"))
    dot=str(input("enter date of transaction:"))
    ttype="w"
    mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
    mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
    mydb.commit()



while(True):
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()
    if ch == '1':
        createAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAmount(self,amount)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    
    
