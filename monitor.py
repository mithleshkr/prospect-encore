import pymysql as py
import getpass as pwd
import sys
import os
import admin as a
#import login as lg


con=py.connect("localhost","root","","final")


def insertProsp():
    prosp_id=int(input("Enter Prospect ID :"))
    prosp_name=input("Enter Prospect Name :")
    prosp_phone=int(input("Enter Prospect Phone :"))
    prosp_add=input("Enter Prospect Address :")
    model=input("Enter Prospect intrested Model :")
    color=input("Enter Prospect intrested Color :")
    dov=input("Enter Date & Time Of Visit(YYYY-MM-DD HH:MM:SS) :")
    hotness=input("Enter Hotness :")

    cu=con.cursor()
    qry="insert into prosp value(%d,'%s',%d,'%s','%s','%s','%s','%s')"%(prosp_id,prosp_name,prosp_phone,prosp_add,model,color,dov,hotness)
    cu.execute(qry)
    con.commit()

    if cu.rowcount>0:
        print("Record Inserted...!!!!")
    else:
        print("Record Not Inserted...!!!!")

def displayProsp():
    cu=con.cursor()
    cu.execute("select * from prosp")

    if cu.rowcount>0:
        print("ID\tName\tPhone\tAddress\tModel\tColor\tDOV\tHotness")
        print("---------------------------------------------------------------")
        for r in cu.fetchall():
                for i in r:
                        print(i,end="\t")
                print()
    else:
        print("No Record found...!!!!")

def updateProsp():
    ch=int(input("1. Phone \n2. Model \n3. Color \n4.Hotness \n5.Back \nEnter your choice : "))
    if ch==1:
        id=int(input("Enter the id of the prospect :"))
        cu=con.cursor()
        cu.execute(("select prosp_id from prosp where prosp_id=%d"%(id)))
        if cu.rowcount>0:
            cu.execute("select prosp_name,prosp_phone from prosp")
            l=cu.fetchone()
            print("Name= %s Phone= %d"%(l[0],l[1]))
            ch=input("Press 'Y' to update the number :")
            if ch=='y' or ch=='Y':
                p=int(input("Enter the new phone number"))
                cu.execute("update prosp set prosp_phone=%d where prosp_id=%d"%(p,id))
                con.commit()
                if cu.rowcount>0:
                    print("Record updated")
                else:
                    print("Record not updated")
            else:
                 MonitorMenu()
        else:
            print("Record Not found")
               
                
            
    elif ch==2:
        id=int(input("Enter the id of the prospect :"))
        cu=con.cursor()
        cu.execute(("select prosp_id from prosp where prosp_id=%d"%(id)))
        if cu.rowcount>0:
            cu.execute("select prosp_name,model from prosp")
            l=cu.fetchone()
            print("Name= %s Model= %s"%(l[0],l[1]))
            ch=input("Press 'Y' to update the model :")
            if ch=='y' or ch=='Y':
                p=input("Enter the new model :")
                cu.execute("update prosp set model='%s' where prosp_id=%d"%(p,id))
                con.commit()
                if cu.rowcount>0:
                    print("Record updated")
                else:
                    print("Record not updated")
            else:
                 MonitorMenu()
        else:
            print("Record Not found")




    elif ch==3:
        id=int(input("Enter the id of the prospect :"))
        cu=con.cursor()
        cu.execute(("select prosp_id from prosp where prosp_id=%d"%(id)))
        if cu.rowcount>0:
            cu.execute("select prosp_name,color from prosp")
            l=cu.fetchone()
            print("Name= %s Color= %s"%(l[0],l[1]))
            ch=input("Press 'Y' to update the color :")
            if ch=='y' or ch=='Y':
                p=input("Enter the new color")
                cu.execute("update prosp set color=%s where prosp_id=%d"%(p,id))
                con.commit()
                if cu.rowcount>0:
                    print("Record updated")
                else:
                    print("Record not updated")
            else:
                 MonitorMenu()
        else:
            print("Record Not found")



    elif ch==4:
        id=int(input("Enter the id of the prospect :"))
        cu=con.cursor()
        cu.execute(("select prosp_id from prosp where prosp_id=%d"%(id)))
        if cu.rowcount>0:
            cu.execute("select prosp_name,hotness from prosp")
            l=cu.fetchone()
            print("Name= %s Hotness= %s"%(l[0],l[1]))
            ch=input("Press 'Y' to update the hotness :")
            if ch=='y' or ch=='Y':
                p=input("Enter new Hotness")
                cu.execute("update prosp set hotness=%s where prosp_id=%d"%(p,id))
                con.commit()
                if cu.rowcount>0:
                    print("Record updated")
                else:
                    print("Record not updated")
            else:
                 MonitorMenu()
        else:
            print("Record Not found")
    elif ch==5:
        MonitorMenu()




def searchProsp():
    ch=int(input("1. Hotness \n2. Prospect ID \n3. Back \nEnter your choice : "))
    cu=con.cursor()
    if ch==1:
        hot=input("Enter Hotness you want to search : ")
        cu.execute("select hotness from prosp where hotness=%s"%(hot))
        if cu.rowcount>0:
            cu.execute("selct * from prosp where hotness=%s"%(hot))
            print("ID\tName\tPhone\tAddress\tModel\tColor\tDOV\tHotness")
            print("----------------------------------------------------------------")
            for r in cu.fetchall():
                    for i in r:
                            print(i,end="\t")
                    print()
        else:
            print("Record not Found")
    
    elif ch==2:
        id=int(input("Enter Prospct ID you want to search : "))
        cu.execute("select prosp_id from prosp where prosp_id=%d"%(id))
        if cu.rowcount>0:
            cu.execute("selct * from prosp where prosp_id=%d"%(id))
            print("ID\tName\tPhone\tAddress\tModel\tColor\tDOV\tHotness")
            print("----------------------------------------------------------------")
            for r in cu.fetchall():
                    for i in r:
                            print(i,end="\t")
                    print()
        else:
            print("Record not Found")
    elif ch==3:
        MonitorMenu()


def changepwd():
    uname=input("Enter Username : ")
    upass=pwd.getpass("Enter Password : ") 
    cu=con.cursor()
    qry="select emp_email,emp_pwd from emp where emp_email='%s' and emp_pwd='%s'"%(uname,upass)
    cu.execute(qry)

    if  cu.rowcount>0:
        newpwd=pwd.getpass("Enter New Password : ")
        conpwd=pwd.getpass("Confirm New Password : ")
        if newpwd==conpwd:
                cu.execute("update emp set emp_pwd=%s where emp_email"%(newpwd,uname))
                cu.commit()
                if cu.rowcount>0:
                    print("Record updated")
                else:
                    print("Record not updated")
        else:
            print("Re-Enter the password Correctly")
            changepwd()
    else:
        print("Record not found")

def MonitorMenu():
    while True:
        ch=int(input("1. Add New Prospect \n2. View All Prospect \n3. Update Prospect \n4. Search Prospect \n5. Change Own Password \n6. Sign Out \nEnter your choice : "))
        if ch==1:
            insertProsp()
        elif ch==2:
            displayProsp()
        elif ch==3:
            updateProsp()
        elif ch==4:
            searchProsp()
        elif ch==5:
            changepwd()
        elif ch==6:
            lg.login()
