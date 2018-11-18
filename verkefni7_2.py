# -*- coding: utf-8 -*-



import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    print ("uuups")
    return None


def er_notandinn_til(u,p):
    notandi_til =False
    database = 'kt_verkqlite.db'
    conn = create_connection(database)
    sql="""Select * from user;"""

    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u or r[1]==p:
            notandi_til = True
    return notandi_til

def passa_notendaupplysingar(u,p):
    notendaupplysingar =False
    database = 'kt_verkqlite.db'
    conn = create_connection(database)
    sql="""Select * from user;"""

    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u and r[1]==p:
            notendaupplysingar = True
    return notendaupplysingar

def nyr_notandi(u,p,n):
    database = 'kt_verkqlite.db'
    conn = create_connection(database)
    if er_notandinn_til(u,p):
        print("notandi til")
    else:
        c = conn.cursor()
        c.execute("""insert into user (user,password,name) values(?,?,?);""",(u,p,n))
        conn.commit()
        conn.close()

"""def main():

    database = 'kt_verkqlite.db'
    conn = create_connection()
    
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        print(row)
     #bæta við notanda


    u=str(input("sláðu inn username"))
    p=str(input("sláðu inn password"))
    n=str(input("sláðu inn name"))

    nyr_notandi(u,p,n)

    c = conn.cursor()
    rows = c.fetchall()

    for row in rows:
        print(row)
main()"""




