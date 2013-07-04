import cgi
import pymysql

print("Content-Type: text/html")
print("")
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
login = form.getvalue('login')
password  = form.getvalue('password')

#Работа с базой
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='pen3souin', db='paintinggamedb')
cur = conn.cursor()
#TODO сделать отлов ошибок MySQL, например на уникальность логина/мыла и т.п
cur.execute("SELECT id FROM pgusers where login=%s and password=%s", (login, password))

id = cur.fetchone()

conn.commit()
cur.close()
conn.close()

print(id[0])