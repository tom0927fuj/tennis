#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
import MySQLdb
import servetiebreak
import returntiebreak
import returnpointcheck

connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Kyamamoto99',
    db='tennis2'
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']

import cgi
form = cgi.FieldStorage()
if form.getfirst('yes'):
    Force=1
elif form.getfirst('no'):
    Force=2
#どうでもいいけど，Force=1とForce=2のときで，中身のif（tiecheck）の部分の書き方微妙に違う
#というか下記でいいのでは
if Force==1:
    cursor.execute("""INSERT INTO forcedornot(forced) VALUES (1)""")
elif Force==2:
    cursor.execute("""INSERT INTO forcedornot(unforced) VALUES (2)""")
connection.commit()

if  Tiecheck==1:
    servetiebreak.py
elif Tiecheck==2:
    returntiebreak.py
else:
    returnpointcheck.py
