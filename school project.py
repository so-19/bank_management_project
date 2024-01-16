#SOURCE CODE FOR BANKING TRANSACTIONS
print("BANK TRANSACTION SERVICE")
print("Welcome To MSD Bank")
print("We offer A variety of services to our customers")
print("Our Motto--We are always with you")#tagline
print('The services we offer are-')
print()
import random
from tabulate import tabulate
import time
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ozs123*")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance float(6),password varchar(10))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount float(6),dot date ,ttype char(1),foreign key (acno) references bank_master(acno))")
mycursor.execute("create table if not exists FD(acno char(4),FDNO varchar(200),AMNT varchar(20),intrest varchar(23),tenure varchar(5))")
mycursor.execute("create table if not exists cards(acno char(4),creditcardnumber varchar(10),CVV char(3),PIN char(4),Credit int(6))")
mydb.commit()
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
def createAccount():
    acno=str(input('Enter account number(only 4 characters):'))
    name=input("Enter name(limit 35 characters):")
    city=str(input("Enter city name:"))
    password=input("Enter Your password:")
    balance=0
    mn=str(input("Enter mobile no.:"))
    if len(mn)==10:
        otp=random.randint(10000,99999)
        print("you will receive an OTP on the screen,Type the OTP when asked")
        print("Your ONE TIME PASSWORD IS::::",otp)
        print('Please wait for some time for the screen to load')
        print('Do not press any key')
        time.sleep(4)
        otpu=int(input('Enter the OTP you received:'))
        if otp==otpu:
            print("Your OTP is correct")
            mycursor.execute("select acno from bank_master")
            data=mycursor.fetchall()
            if (acno,) not in data:
                mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"','"+password+"')")
                mydb.commit()
                print("Account is successfully created!!!")
                print('Thank you for creating an account with our bank')
                print()
            else:
                print("The account number is already taken")
                print("Please select another account number")
                print("Sorry for the inconvenience caused")
                createAccount()
        else:
            print("You have entered a wrong OTP")
            createAccount()
    else:
        print("You have entered an invalid Mobile Number")
        createAccount()
    print()
    
#PROCEDURE FOR UPDATIONG DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
def depositAmount():
    acno=str(input('Enter Account Number:'))
    dp=float(input("Enter amount to be deposited:"))
    dot=str(input("enter date of transaction(year/month/date):"))
    password=input("Enter Password:")
    ttype="d"
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]
    if pwd3==password:
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("Money has been deposited successully!!!")
        print()
    else:
        print("You are an invalid user for this account")
        print("Passwords do not match")
    print()

#PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT
def withdrawMoney():
    acno=str(input("Enter account number:"))
    wd=float(input("Enter amount to be withdrawn:"))#d
    dot=str(input("enter date of transaction(year/month/date):"))
    password=input("Enter Password:")
    ttype="w"
    query="select balance from bank_master where acno={}.".format(acno)
    mycursor.execute(query)
    x=mycursor.fetchone()#tuple 
    b=str(wd)
    c=tuple(b)
    d="".join([x[0] for x in c])#string
    e=str(x)
    f=tuple(e)
    g="".join([x[0] for x in f])#string
    s=g[1:len(g)-2]
    h=int(d)
    i=int(s)
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pn=mycursor.fetchone()
    pn1=str(pn)
    pn2="".join([x[0] for x in pn1])
    pn3=pn2[2:len(pn2)-3]
    if pn3==password:
        if h <= i:
            mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
            mydb.commit()
            print('Transaction Successfully Done')
        else:
            print()
            print("Insufficient balance in account!!!!")
            print("Please withdraw amount of money less than",i)
            print()
            withdrawMoney()
    else:
        print("You are an invalid user for this account!!!")
        print("Passwords do not match")
    print()
    
def Showaccount():
    acno=str(input("Enter account number:"))
    password=input("Enter Password:")
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pn=mycursor.fetchone()
    pn1=str(pn)
    pn2="".join([x[0] for x in pn1])
    pn3=pn2[2:len(pn2)-3]
    mycursor.execute("select acno from bank_master")
    data=mycursor.fetchall()
    if (acno,) not in data:
        print("This account does not exist with our bank")
        print("You cannot transfer money to this bank account")
        print("Please create an account first for transferring the money")
        print()
    else:
        if pn3==password:
            print("1=See Balance")
            print("2=See Name")
            print("3=See City")
            print("4=See Mobile number")
            print("5=See Password")
            print()
            ch=int(input("Enter the option you want to see:"))
            if ch==1:
                mycursor.execute("select balance from bank_master where acno='"+acno+"'")
                bal=mycursor.fetchone()
                a=list(bal)
                print("Your Balance is:",str(a))
                print()
            elif ch==2:
                mycursor.execute("select name from bank_master where acno='"+acno+"'")
                n=mycursor.fetchone()
                n1=str(n)
                n2="".join([x[0] for x in n1])
                n3=n2[2:len(n2)-3]
                print("Your name is:",n3)
                print()
            elif ch==3:
                mycursor.execute("select city from bank_master where acno='"+acno+"'")
                cit=mycursor.fetchone()
                cit1=str(cit)
                cit2="".join([x[0] for x in cit1])
                cit3=cit2[2:len(cit2)-3]
                print("Your city is:",cit3)
                print()
            elif ch==4:
                mycursor.execute("select mobileno from bank_master where acno='"+acno+"'")
                mob=mycursor.fetchone()
                mob1=str(mob)
                mob2="".join([x[0] for x in mob1])
                mob3=mob2[2:len(mob2)-3]
                print("Your mobile number is:",mob3)
                print()
            elif ch==5:
                mycursor.execute("select password from bank_master where acno='"+acno+"'")
                pw=mycursor.fetchone()
                pw1=str(pw)
                pw2="".join([x[0] for x in pw1])
                pw3=pw2[2:len(pw2)-3]
                print("Your password is:",pw3)
                print()
        else:
            print("You are an invalid user")
            print("Please enter correct details")
            print("Passwords do not match")
            print()

def Loan():#User account if not there code
    acno=str(input("Enter Account number:"))
    password=input("Enter your Password:")
    dot=str(input("Enter date of transaction(year/month/date):"))
    p=int(input("Enter loan amount in rupees:"))
    n=int(input("Enter number of Months for loan:"))
    ttype="d"
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    ln=mycursor.fetchone()
    ln1=str(ln)
    ln2="".join([x[0] for x in ln1])
    ln3=ln2[2:len(ln2)-3]
    if ln3==password:
        print("Rate of interest=11%")
        r=11
        r1=r/12
        r2=r1/100
        a1=p*r2*(1+r2)**n
        a2=(1+r2)**n-1 #EMI = [P x (R/100) x {1+(R/100)}^N]/[{1+(R/100)}^(N-1)]
        a3=a1/a2
        print("EMI per month",a3)
        print("The loan money will be deposited in your account")
        print('Wait for few seconds for the screen to be loaded')
        print('We appreciate your patience')
        time.sleep(3)
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(p)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(p)+"' where acno='"+acno+"'")
        mydb.commit()
        print("Amount is successfully deposited")
        print()
    else:
        print("You are an invalid user for this account")
        print("Passwords do not match")
    print()

def ModifyAccount():
    acno=str(input("Enter account number:"))
    password=input("Enter Password:")
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]
    if pwd3==password:
        print("What do you want to Modify")
        print("1=Name")
        print("2=City")
        print("3=Mobile number")
        print("4=Password")
        abc=int(input("Enter your choice:"))
        if abc==1:
            name=input("Enter name(limit 35 characters):")
            mycursor.execute("update bank_master set name='"+name+"' where acno='"+acno+"'")
            mydb.commit()
            print("Your account has been successfully updated")
            print()
        elif abc==2:
            city=input("Enter City name:")
            mycursor.execute("update bank_master set city='"+city+"' where acno='"+acno+"'")
            mydb.commit()
            print("Your account has been successfully updated")
            print()
        elif abc==3:
            mn=str(input("Enter your new Mobile number:"))
            mycursor.execute("update bank_master set mobileno='"+mn+"' where acno='"+acno+"'")
            mydb.commit()
            print("Your account has been successfully updated")
            print()
        elif abc==4:
            pwd=input("Enter your new password:")
            mycursor.execute("update bank_master set password='"+pwd+"' where acno='"+acno+"'")
            mydb.commit()
            print("Your account has been successfully updated")
            print()
    else:
        print("You are an invalid user")
        print("Passwords do not match")
        print()

def TransferMoney():
    acno=str(input("Enter account number from where amount to be withdrawn:"))
    acno1=str(input("Enter account number from where amount to be deposited:"))
    amt=float(input("Enter amount to be transferred:"))
    ttype="t"
    dot=str(input("enter date of transaction(year/month/date):"))
    password=input("Enter Password:")
    query="select balance from bank_master where acno={}.".format(acno)
    mycursor.execute(query)
    x=mycursor.fetchone()
    e=str(x)
    f=tuple(e)
    g="".join([x[0] for x in f])#string
    s=g[1:len(g)-2]
    i=int(s)
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]
    mycursor.execute("select acno from bank_master")
    data=mycursor.fetchall()
    if (acno1,) not in data:
        print("This account does not exist with our bank")
        print("You cannot transfer money to this bank account")
        print("Please create an account first for transferring the money")
        print()
    else:
        if pwd3==password:
            if amt<=i:
                print("Acesss granted")
                print()
                mycursor.execute("insert into banktrans values('"+acno1+"','"+str(amt)+"','"+dot+"','"+ttype+"')")
                mycursor.execute("update bank_master set balance=balance+'"+str(amt)+"' where acno='"+acno1+"'")
                mycursor.execute("insert into banktrans values('"+acno+"','"+str(amt)+"','"+dot+"','"+ttype+"')")
                mycursor.execute("update bank_master set balance=balance-'"+str(amt)+"' where acno='"+acno+"'")
                mydb.commit()
                print("Transaction was successful")
                print()
            else:
                 print("You do not have sufficient balance")
                 print("Please deposit money to make a successfull transfer")
                 print()
        else:
            print("You are an invalid user")
            print("Passwords do not match")
            print()

def TransactionSummary():
    acno=str(input("Enter account number:"))
    password=input("Enter Password:")
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]
    mycursor.execute("select acno from bank_master")
    data=mycursor.fetchall()
    if (acno,) not in data:
        print("This account does not exist with our bank")
        print("Please create an account with our bank to avail this feature")
        print()
    else:
        if pwd3==password:
            print("Showing your Transaction summary")
            print()
            mycursor.execute("select * from banktrans where acno='"+acno+"'")
            myresult=mycursor.fetchall()
            print(tabulate(myresult,headers=['ACNO','Amount','Date','TTYPE'],tablefmt='psql'))
            #myresult=mycursor.fetchall()
            #print(''.format(myresult))
            print("This is your transaction summary")
            print("t=Transferring of money")
            print("d=Deposition of money")
            print("w=Withdrawal of money")
            print()
        else:
            print("You are an invalid user!!!!")
            print("Passwords do not match")
            print()

def FD():
    acno=str(input('enter account no:'))
    password=input("Enter Password:")
    mycursor.execute("select acno from bank_master")
    data=mycursor.fetchall()
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]    
    if (acno,) not in data:
        print('You cannot avail this feature as you do not have an account')
        print("Please create an account first")
        print()
    else:
        if pwd3==password:
            print("Minimum amount of rupees for FD is rupees 10000")
            print("FD amount will be taken from your account so keep sufficient balance")
            AMNT=int(input('enter amount to be deopsited in FD:'))
            if AMNT<10000:
                print("Minimum amount of FD is 10000 rupees")
                print()
            else:
                mycursor.execute("select balance from bank_master where acno={}".format(acno))
                m1=mycursor.fetchone()
                m2=str(m1)
                m3="".join([x[0] for x in m2])
                m4=m3[1:len(m3)-2]
                m5=int(m4)
                if m5<AMNT:
                    print('Insufficient balance in your account to create FD')
                    print()
                else:
                    FDNO=random.randint(999999999,10**10)
                    tenure=int(input("Enter tenure for the Fixed deposit(in years):"))
                    rateofintrest=ROI=7
                    intrest=AMNT*ROI*tenure/100
                    print('intrest is calculated annualy')
                    print("FD tenure is:",tenure)
                    print("Rate of interest per year is 7%")
                    mycursor.execute("update bank_master set balance=balance-'"+str(AMNT)+"' where acno='"+acno+"'")
                    mycursor.execute('insert into FD values("{}",{},{},{},{})'.format(acno,FDNO,AMNT,intrest,tenure))
                    mydb.commit()
                    print('FD created succesfully')
                    print("Your FD number is:",FDNO)
                    print('You will get intrest after your tenure is:',intrest,'every year')
                    print("Interest per year is:",intrest/tenure)
                    print()
        else:
            print('You are an invalid user')
            print("Passwords do not match")
            print()
        

def cards():
    acno=str(input('enter account no:'))
    password=input("Enter Password:")
    mycursor.execute("select acno from bank_master")
    data=mycursor.fetchall()
    mycursor.execute("select password from bank_master where acno={}".format(acno))
    pwd=mycursor.fetchone()
    pwd1=str(pwd)
    pwd2="".join([x[0] for x in pwd1])
    pwd3=pwd2[2:len(pwd2)-3]
    if (acno,) not in data:
        print('You cannot avail this feature as you do not have an account')
        print("Please create an account first")
        print()
    else:
        if pwd3==password:
            creditcarnumber=random.randint(999999999,10**10)
            cc1=str(creditcarnumber)
            CVV=random.randint(0,999)
            CVV1=str(CVV)
            PIN=str(input('enter your 4 digit PIN:'))
            Credit=0
            Credit1=str(Credit)
            mycursor.execute("insert into cards values('"+acno+"','"+cc1+"','"+CVV1+"','"+PIN+"','"+Credit1+"')")
            mydb.commit()
            print("Your credit card number is:",cc1)
            print("Your CVV is:",CVV1)
            print("Enjoy your new Credit card")
            print('credit card succesfully created')
            print()
        else:
            print('You are an invalid user')
            print("Passwords do not match")
            print()

def DeleteAccount():
    acno=str(input('enter account no:'))
    ans=input("Are you sure you want to delete your account:")
    if ans=='yes':
        mycursor.execute("select acno from bank_master")
        data=mycursor.fetchall()
        if (acno,) not in data:
            print('We do not have any account number with the above given entry')
            print("Please enter a valid account number")
            print()
        else:
            password=input("Enter Password:")
            mycursor.execute("select password from bank_master where acno={}".format(acno))
            pwd=mycursor.fetchone()
            pwd1=str(pwd)
            pwd2="".join([x[0] for x in pwd1])
            pwd3=pwd2[2:len(pwd2)-3]
            if pwd3==password:
                print("We regret that you are leaving our bank")
                mycursor.execute('SET FOREIGN_KEY_CHECKS=0;')
                mycursor.execute("delete from bank_master where acno={}".format(acno))
                mydb.commit()
                mycursor.execute('SET FOREIGN_KEY_CHECKS=1;')
                mydb.commit()
                print("Your account is successfully deleted")
                print("Thank you for being our customer")
                print()
            else:
                print("You have entered a wrong password")
                print("You cannot be granted access")
                print()
                                                    
while True:
    print("1=Create account")
    print("2=Deposit money")
    print("3=Withdraw money")
    print("4=Display Account")
    print("5=Loan Application")
    print("6=Modify account details")
    print("7=Transfer Money")
    print("8=Transaction summary")
    print("9=FD creation") 
    print("10=Credit Card")
    print("11=Delete Account")
    print("12=Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        createAccount()
    elif ch==2:
        depositAmount()
    elif ch==3:
        withdrawMoney()
    elif ch==4:
        Showaccount()
    elif ch==5:
        Loan()
    elif ch==6:
        ModifyAccount()
    elif ch==7:
        TransferMoney()
    elif ch==8:
        TransactionSummary()
    elif ch==9:
        FD()
    elif ch==10:
        cards()
    elif ch==11:
        DeleteAccount()
    elif ch==12:
        break
    else:
        print()
        print('Oops!!!! Wrong option, Please enter a valid option number')
        print()
        

