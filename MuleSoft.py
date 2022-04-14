import sqlite3
def sqlcon():
    global sqliteConnection,cur
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
def sqlcreate():
    query="create table Movies(name varchar(45),actor varchar(50),actress varchar(50),director varchar(50),year_of_release Integer);"
    cur.execute(query)
def sqlinsert():
    query1="Insert into Movies values('3 idiots','Aamir Khan','Kareena Kapoor','Rajkumar Hiarni','2009');"
    query2="Insert into Movies values('James','Puneeth Rajkumar','Priya Anand','Chetan Kumar','2022');"
    query3="Insert into Movies values('Kgf2','Yash','Srinidhi Shetty','Prashanth neel','2022');"
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    sqliteConnection.commit()
def sqlselect():
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
    query1="select * from Movies;"
    query2="select * from Movies where actor='Yash';"
    cur.execute(query1)
    result=cur.fetchall()   
    cur.execute(query2)
    result2=cur.fetchall()   
    print(result)
    print(result2)
sqlcon()
sqlcreate()
sqlinsert()
sqlselect()
