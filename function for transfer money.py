def TransferMoney():
    acno=str(input("Enter account number from where amount to be withdrawn:"))
    acno1=str(input("Enter account number from where amount to be deposited:"))
    amt=int(input("Enter amount to be transferred:"))
    ttype="t"
    dot=str(input("enter date of transaction:"))
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
    if pwd3==password:
        if amt<=i:
            print("Acesss granted")
            mycursor.execute("insert into banktrans values('"+acno1+"','"+str(amt)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance+'"+str(amt)+"' where acno='"+acno1+"'")
            mycursor.execute("insert into banktrans values('"+acno+"','"+str(amt)+"','"+dot+"','"+ttype+"')")
            mycursor.execute("update bank_master set balance=balance-'"+str(amt)+"' where acno='"+acno+"'")
            mydb.commit()
            print("Transaction was successful")
        else:
            print("You do not have sufficient balance")
    else:
        print("You are an invalid user")
        print("Passwords do not match")
            
        
        
