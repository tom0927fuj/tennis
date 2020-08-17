#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-s
import MySQLdb
import cgi
import servetiebreak
import returntiebreak
import servepointcheck
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
how_s=""
how_v=0
if form.getfirst('serve'):
    Howwinner=1
    how_s="serve"
    how_v=1
elif form.getfirst('rally'):
    Howwinner=2
    how_s="ornot"
    how_v=2
cur_str="INSERT INTO howwinner("+how_s+") VALUES("+how_v+")"
#もし可能であれば，こうしたほうが簡潔
#ただこれでexecuteできるかは分からないので，そっちで試してください．
#もしexecuteできるのであれば，1point_losenetplay，1point_winnetplay，1pointre_netplay，も同様にやればいいと思います．
cursor.execute(cur_str)
connection.commit()
if Tiecheck==0:
    servepointcheck.py
elif Tiecheck==1:
    servetiebreak.py
elif Tiecheck==2:
    returntiebreak.py
