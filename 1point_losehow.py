#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-

import MySQLdb
import cgi
import pointhyoji
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
    <h1>エラーですか？（1=yes,2=no)</h1>
    <form action='1point_error.py' method='POST'>
    <input type='submit' name='yes' value='yes' class='button'><br></br>
    <input type='submit' name='no' value='no' class='button'>
    </form>
    <form action='chosei.py' method='POST'>
    <input type='submit' name='調整' value='調整'>
    </form>""")
    print(string)
    pointhyoji.hyoji()

form = cgi.FieldStorage()
if form.getfirst('yes'):
    Losenet=1
elif form.getfirst('no'):
    Losenet=2

if Losenet==1:
    cursor.execute("""INSERT INTO net(lose) VALUES (1)""")
    connection.commit()
    if Tiecheck==0:
        servepointcheck.py
    elif Tiecheck==1:
        servetiebreak.py
    elif Tiecheck==2:
        returntiebreak.py
elif Losenet==2:
    how()
