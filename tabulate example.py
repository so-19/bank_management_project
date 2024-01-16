import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ozs123*")
mycursor=mydb.cursor()
mycursor.execute("use bank")
mycursor.execute('select acno,name from bank_master')
myresult=mycursor.fetchall()
print(tabulate(myresult,headers=['ACNO','NAME'],tablefmt='psql'))
