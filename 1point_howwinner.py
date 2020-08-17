#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-s
import MySQLdb
import cgi
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Kyamamoto99',
    db='tennis2'
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tiecheck`) FROM `score`")
Tiecheck=cursor.fetchone()['COUNT(`tiecheck`)']

form = cgi.FieldStorage()
if form.getfirst('serve'):
    Howwinner=1
elif form.getfirst('rally'):
    Howwinner=2
if Howwinner==1:
    cursor.execute("""INSERT INTO howwinner(serve) VALUES (1)""")
    connection.commit()
    if Tiecheck==0:
        import servepointcheck
        servepointcheck.py
    elif Tiecheck==1:
        import servetiebreak
        servetiebreak.py
    elif Tiecheck==2:
        import returntiebreak
        returntiebreak.py
elif Howwinner==2:
    cursor.execute("""INSERT INTO howwinner(ornot) VALUES (2)""")
    connection.commit()
    if Tiecheck==0:
        import servepointcheck
        servepointcheck.py
    elif Tiecheck==1:
        import servetiebreak
        servetiebreak.py
    elif Tiecheck==2:
        import returntiebreak
        returntiebreak.py