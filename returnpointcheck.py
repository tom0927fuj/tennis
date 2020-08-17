#!C:\Users\yamamoto\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf -8  -*-
print("Content-Type: text/html\n")
import MySQLdb
import pointre_win
import point_win
import result
import servetiebreak
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Kyamamoto99',
    db='tennis2'
)
cursor= connection.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT COUNT(`player1`) FROM `score`")
player1=cursor.fetchone()['COUNT(`player1`)']
Player1=int(player1)
cursor.execute("SELECT COUNT(`player2`) FROM `score`")
player2=cursor.fetchone()['COUNT(`player2`)']
Player2=int(player2)
cursor.execute("SELECT COUNT(`player1`) FROM `setscore`")
player1game=cursor.fetchone()['COUNT(`player1`)']
Player1game=int(player1game)
cursor.execute("SELECT COUNT(`player2`) FROM `setscore`")
player2game=cursor.fetchone()['COUNT(`player2`)']
Player2game=int(player2game)
def game():
    if Player1>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player1) VALUES (1)")
            connection.commit()
            point_win.py
        else:
            pointre_win.py
    elif Player2>3:
        if abs(Player1-Player2)>1:
            cursor.execute("DELETE FROM score")
            cursor.execute("INSERT INTO setscore(player2) VALUES (2)")
            connection.commit()
            point_win.py
        else:
            pointre_win.py
    else:
        pointre_win.py
if Player1game>5 or Player2game>5:
    if abs(Player1game-Player2game)>2:
        result.py
    elif Player1game==6 and Player2game==6:
        cursor.execute("INSERT INTO score(tiecheck) VALUES (1)")
        connection.commit()
        servetiebreak.py
    elif Player1game==7 or Player2game==7:
        result.py
    else:
        game()
else:
    game()
