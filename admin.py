import os
import sys
import pymysql as py
import getpass as pwd
import monitor as m
#import login as lg

con=py.connect("localhost","root","","final")

def createAcc():
    ch=int(input("1. Add Prospect Account \n2. Add Admin Account  \n3.Back \nEnter your choice...: "))
    if ch==1:
        insertProsp()
    elif ch==2:
        emp_id=int(input("Enter Employee ID :"))
        emp_pwd=input("Enter Employee Password :")
        emp_name=input("Enter Employee Name :")
        emp_phone=int(input("Enter Employee Phone :"))
        emp_email=input("Enter Employee E-Mail :")
        emp_status=input("Enter Employee Status :")
        emp_role=input("Enter Employee Role :")
        cu=con.cursor()
        qry="insert into emp value(%d,'%s','%s',%d,'%s','%s','%s')"%(emp_id,emp_pwd,emp_name,emp_phone,emp_email,emp_status,emp_role)
        cu.execute(qry)
        con.commit()
        if cu.rowcount>0:
            print("Record Inserted...!!!!")
        else:
            print("Record Not Inserted...!!!!")
        
    elif ch==3:
        AdminMenu()


def displayEmp():
    cu=con.cursor()
    cu.execute("select * from emp")

    if cu.rowcount>0:
        print("ID\tPassword\tName\tPhone\tE-Mail\tStatus\tRole")
        print("-------------------------------------------------------")
        for r in cu.fetchall():
                for i in r:
                        print(i,end="\t")
                print()
    else:
        print("No Record found...!!!!")


def chnageEpwd():
    ch=int(input("1. Self \n2. Others  \n3.Back \nEnter your choice...: "))
    if ch==1:
        changepwd()
    elif ch==2:
        id=int(input("Enter the ID :"))
        cu=con.cursor()
        cu.execute(("select emp_id from emp where emp_id=%d"%(id)))
        if cu.rowcount>0:
            newpwd=pwd.getpass("Enter New Password : ")
            conpwd=pwd.getpass("Confirm New Password : ")
            if newpwd==conpwd:
                    cu.execute("update emp set emp_pwd=%s where emp_id"%(newpwd,id))
                    cu.commit()
                    if cu.rowcount>0:
                        print("Record updated")
                    else:
                        print("Record not updated")
        else:
                print("Re-Enter the password Correctly")
    
    
    
    elif ch==3:
        AdminMenu()

def status():
        id=int(input("Enter the ID :"))
        cu=con.cursor()
        cu.execute(("select emp_id from emp where emp_id=%d"%(id)))
        if cu.rowcount>0:
            cu.execute("select * from emp where emp_id=%d"%(id))
            print("ID\tPassword\tName\tPhone\tE-Mail\tStatus\tRole")
            print("-------------------------------------------------------")
            for r in cu.fetchall():
                        for i in r:
                                print(i,end="\t")
                        print()
        else:
                print("Record not Found")
        ch=int(input("\n\n1.Change Status \n2.Back \nEnter your choice :"))
        if ch==1:
            st=input("Enter Status (Activate/Deactivate): ")
            cu.execute("update emp set emp_status=%s where emp_id=%d"%(st,id))
            con.commit()
            if cu.rowcount>0:
                    print("Record updated")
            else:
                    print("Record not updated")
         
        elif ch==2:
            AdminMenu()



def AdminMenu():
    while True:
        ch=int(input("1. Create Account \n2. View All Employees \n3. View All Prospect \n4. Change Password \n5. Search Prospect \n6. Change Status \n7. Sign Out \nEnter your choice : "))
        if ch==1:
            createAcc()
        elif ch==2:
            displayEmp()
        elif ch==3:
            m.displayProsp()
        elif ch==4:
            changeEpwd()
        elif ch==5:
            m.searchProsp()
        elif ch==6:
            status()
        elif ch==7:
            lg.login()
        
            
