import mysql.connector


try:
    con = mysql.connector.connect(user='root',password='jll;',host='127.0.0.1',database='sirene')
except mysql.connector.Error as err:
    print('erreur:',err.msg)
else:
    print('connextion réussis')
    con.close()