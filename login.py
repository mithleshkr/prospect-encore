import getpass as pwd
import pymysql as py
import sys
import os     
import monitor as m
import admin as a
conn=py.connect("localhost","root","","final")


class login():
    
    try:
        print("default uname = mith@mail.com and password = 123")
        uname=input("Enter Username : ")
        upass=pwd.getpass("Enter Password : ") 
        cu=conn.cursor()
        qry="select emp_email,emp_pwd,emp_name,emp_role from emp where emp_email='%s' and emp_pwd='%s'"%(uname,upass)
        cu.execute(qry)

        if  cu.rowcount>0:
             l=cu.fetchone()
             os.system("pause")
             print("********************************************************************************")
             print("\t\t\t\tWELCOME %s "%(l[2]))
             print("********************************************************************************")
             
             for i in range(0,5000):
                 pass
             ch=input("Press Y to enter into the Menu : ")
             if ch=='y' or ch=='Y':
                 os.system('cls')
                 if l[3]=="Admin" or l[3]=="admin":
                     a.AdminMenu()
                 else:
                     m.MonitorMenu()
             else:
                 print("**********************************************************************************")
                 print("********************************ThankYou For Visiting*****************************")
                 print("**********************************************************************************")
                 for i in range(0,10000):
                     pass
                 sys.exit()
        else:
            print("Invalid UserName and PassWord")
    except:
        print("Error")
        

