#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
import MySQLdb
import cgi
import returnpointcheck
import servetiebreak
import returntiebreak
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Kyamamoto99',
    db='tennis2'
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']
print(Tiecheck)
form = cgi.FieldStorage()
if form.getfirst('serve'):
    Howwinner=1
elif form.getfirst('rally'):
    Howwinner=2
if Howwinner==1:
    if Tiecheck==0:
        returnpointcheck.py
    elif Tiecheck==1:
        servetiebreak.py
    elif Tiecheck==2:
        returntiebreak.py
elif Howwinner==2:
    cursor.execute("""INSERT INTO howwinner(ornot) VALUES (2)""")
    connection.commit()
    if Tiecheck==0:
        returnpointcheck.py
    elif Tiecheck==1:
        servetiebreak.py
    elif Tiecheck==2:
        returntiebreak.py
else:
    print("前に戻ってください")
