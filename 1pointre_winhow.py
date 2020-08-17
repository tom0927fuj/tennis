#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-

import MySQLdb
import pointhyoji
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

def how():
    string = ("""
    <!DOCTYPE html>
    <html lang='ja'>
    <head>
    <meta charset='utf-8/'>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <title>sample1</title>
    </head>
    <body>
    <h1>エラーですか？</h1>
    <form action='1pointre_error.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'></form>
    <form action='choseireturn.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>
    """)
    print(string)
    pointhyoji.hyoji()

import cgi
form = cgi.FieldStorage()
if form.getfirst('yes'):
    Winnet=1
elif form.getfirst('no'):
    Winnet=2

if Winnet==1:
    cursor.execute("""INSERT INTO net(win) VALUES (1)""")
    connection.commit()
    if Tiecheck==0:
        returnpointcheck.py
    elif Tiecheck==1:
        servetiebreak.py
    elif Tiecheck==2:
        returntiebreak.py
elif Winnet==2:
    how()
else:
    print("前に戻ってください")
