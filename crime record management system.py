import mysql.connector
import time
from datetime import date

global conn,cursor
conn=mysql.connector.connect(host="localhost",database="crime",user="root",password="kasak1665")
cursor=conn.cursor()0

def clear():
    for _ in range(65):
        print()

def introduction():
    msg='''
           CRIME RECORD MANAGEMENT SYSTEM
           -An Introduction
           Crime record management are the most important part of any modern society for better controlling crime.It uses to record crime activities of criminals. 
The law enforcement authority can preserve records of the criminals and search for any criminal using the system.
We have used Python, MYSQL to develop this system. The project is very user-friendly and helful for higher authorities.  '''
    for x in msg:
        print(x,end='')
        time.sleep(0.002)
    wait=input('press any key to continue.....')

def made_by():
    msg='''
           Crime Record information system made by   :  kasak gupta and anika
           Roll No                                   :  
           School Name                               :  jinvani bharti public school
           session                                   :  2022-23

           Thanks for evaluating my project.'''
    for x in msg:
        print(x,end='')
        time.sleep(0.002)
    wait=input("press any key to continue....")

def display_records():
    cursor.execute('select* from crime_record;')
    records=cursor.fetchall()
    for row in records:
        print(row)

def login():
    while True:
        clear()
        uname=input("enter your id:")
        upass=input("enter your password:")
        cursor.execute('select * from login where name="{}" and pwd="{}"'.format(uname,upass))
        cursor.fetchall()
        rows= cursor.rowcount
        if rows!=1:
            print("invalid login details .....try again")
        else:
            print("you are eligible for operating this system......")
            print("\n\n\n")
            print("press any key to continue .........")
            break

def add_crime_type():
    clear()
    offence_name=input('enter offence name:')
    ipc_section=input('enter IPC Section applied for this offence:')
    comment=input('enter any information:')
    sql='insert into crime_type (offence_name,ipc_section,comment) values("{}","{}","{}");'.format(offence_name,ipc_section,comment)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New offence type added.....')
    wait=input('\n\n\n press any key to continue.........')

def add_record():
    clear()
    d=input("enter crime date:")
    offencetype=int(input("enter offence id"))
    name=input("enter complainee name")
    address=input("enter your address")
    num=input("enter phone number")
    status=input("enter crime status")
    updatedate=date.today()
    query='insert into crime_record(c_date,offence_type,complaint_by,address,phone_no,status,update_date)values("{}","{}","{}","{}","{}","{}","{}");'.format(d,offencetype,name,address,num,status,updatedate)
    cursor.execute(query)
    conn.commit()
    
    print('\n\n new crime record added.....')
    
    wait=input('\n\n\n press any key to continue........')

def modify_crime_type_record():
    clear()
    print(' MODIFY CRIME TYPE SCREEN')
    print('1. offence name \n')
    print('2. IPC Section\n')
    print('3. Comment \n')
    choice=int(input('enter your choice:'))
    field=' '
    if choice==1:
        crime_id=int(input('enter crime type id'))
        value=input('enter new offence name:')
        query="UPDATE crime_type SET offence_name=%s WHERE id=%s"
        data=(value,crime_id)
        cursor.execute(query,data)
        conn.commit()
    if choice==2:
        crime_id=int(input('enter crime type id:'))
        value=input('enter new ipc section:')
        query="UPDATE crime_type SET ipc_section=%s WHERE id =%s"
        data=(value,crime_id)
        cursor.execute(query,data)
        conn.commit()
    if choice==3:
        crime_id=int(input('enter crime type id:'))
        value=input('enter new values:')
        query="UPDATE crime_type SET comment=%s WHERE id=%s"
        data=(value,crime_id)
        cursor.execute(query,value)
        conn.commit()

    print('record updated successfully..............')
    wait=input('\n\n\npress any key to continue...........')


def modify_record():
    clear()
    print("1. crime date \n")
    print("2. offence type \n")
    print("3. complaint by \n")
    print("4. address \n")
    print("5. phone no \n")
    print("6. status \n")
    choice=int(input("enter your choice:"))
    field=' '
    if choice==1:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new date:')
        sql='UPDATE crime_record SET c_date=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sql,data)
        conn.commit()

    if choice==2:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new offence type:')
        sql='UPDATE crime_record SET offence_type=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sql,data)
        conn.commit()

    if choice==3:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new complaint_by:')
        sql='UPDATE crime_record SET complaint_by=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sql,data)
        conn.commit()

    if choice==4:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new address:')
        sql='UPDATE crime_record SET address=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sql,data)
        conn.commit()

    if choice==5:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new phone_no:')
        sql='UPDATE crime_record SET phone_no=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sql,data)
        conn.commit()

    if choice==6:
        print('\n\n\n')
        crime_id=input('enter crime record id:')
        value=input('enter new status:')
        sql='UPDATE crime_record SET status=%s WHERE id=%s'
        data=(value,crime_id)
        cursor.execute(sqldata)
        conn.commit()


    print('record updated successfully.............')
    wait=input('\n\n\n press any key to continue..........')


def search_menu():
    clear()
    print(' SEARCH CRIME RECORD SCREEN ')
    print("1. crime date \n")
    print("2. offence type \n")
    print("3. complaint by \n")
    print("4. address \n")
    print("5. phone no \n")
    print("6. status \n")
    choice=int(input("enter your choice:"))
    field=' '
    if choice==1:
        value=input("enter date you search for")
        sql="Select * from crime_record where c_date='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall()
        count=cursor.rowcount
        print(data)
    if choice==2:
        value=int(input("enter offence type you search for"))
        sql="Select * from crime_record where offence_type='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall()
        count=cursor.rowcount
        print(data)
    if choice==3:
        value=input("enter compailt by you search for")
        sql="Select * from crime_record where complaint_by='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall()
        count=cursor.rowcount
        print(data)
    if choice==4:
        value=input("enter address you search for")
        sql="Select * from crime_record where address='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall
        count=cursor.rowcount
        print(data)
    if choice==5:
        value=input("enter phone_no you search for")
        sql="Select * from crime_record where phone_no='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall()
        count=cursor.rowcount
        print(data)
    if choice==6:
        field='status'
        value=input("enter status you search for")
        sql="Select * from crime_record where status='"+value+"'"
        cursor.execute(sql)
        data=cursor.fetchall()
        count=cursor.rowcount
        print(data)
    
    wait=input("\n\n\npress any key to continue...........")


def main_menu():
    login()
    introduction()

    while True:
        clear()
        print('CRIME RECORD INFORMATION SYSTEM')
        print('*'*100)
        print("\n1.add new record")
        print("\n2. add new crime type record")
        print("\n3. modify crime type record")
        print("\n4. modify crime record")
        print("\n5. search crime database")
        print("\n6. close application")
        print('\n\n')
        choice=int(input('enter your choice....'))

        if choice==1:
            add_record()
        if choice==2:
            add_crime_type()
        if choice==3:
            modify_crime_type_record()
        if choice==4:
            modify_record()
        if choice==5:
            search_menu()
        if choice==6:
            break
    made_by()

if __name__=="__main__":
    main_menu()
            
        
 
        
