#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-

import MySQLdb
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
if Force==1:
    cursor.execute("""INSERT INTO forcedornot(forced) VALUES (1)""")
    connection.commit()
    if  Tiecheck==1:
        import servetiebreak
        servetiebreak.py
    elif Tiecheck==2:
        import returntiebreak
        returntiebreak.py
    else:
        import returnpointcheck
        returnpointcheck.py    
elif Force==2:
    cursor.execute("""INSERT INTO forcedornot(unforced) VALUES (2)""")
    connection.commit()
    if Tiecheck==0:
        import returnpointcheck
        returnpointcheck.py
    elif Tiecheck==1:
        import servetiebreak
        servetiebreak.py
    elif Tiecheck==2:
        import returntiebreak
        returntiebreak.py