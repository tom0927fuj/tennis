#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
import MySQLdb
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Kyamamoto99',
    db='tennis2'
)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`tieplayer1`) FROM `score`")
Tieplayer1=cursor.fetchone()['COUNT(`tieplayer1`)']

cursor.execute("SELECT COUNT(`tieplayer2`) FROM `score`")
Tieplayer2=cursor.fetchone()['COUNT(`tieplayer2`)']

point=Tieplayer1+Tieplayer2
def tiebreak():
    if point % 4 == 0 or point % 4 == 3:
        import pointre_win
        pointre_win.py
    else:
        import point_win
        point_win.py   

if Tieplayer1>6 or Tieplayer2>6:
    if abs(Tieplayer1-Tieplayer2)>1:
        import result
        result.py
    else:
        tiebreak()
else:
    tiebreak()