import cgi
import pymysql
import os

print("Content-Type: text/html")
print("")
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
login = form.getvalue('login')
password  = form.getvalue('password')

#Получаем переменные окружения
host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
port = os.environ['OPENSHIFT_MYSQL_DB_PORT']
user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
passwd = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
db = os.environ['OPENSHIFT_APP_NAME']

#Работа с базой
conn = pymysql.connect(host, port, user, passwd, db)
cur = conn.cursor()
#TODO сделать отлов ошибок MySQL, например на уникальность логина/мыла и т.п
cur.execute("SELECT id FROM pgusers where login=%s and password=%s", (login, password))

id = cur.fetchone()

conn.commit()
cur.close()
conn.close()

print(id[0])