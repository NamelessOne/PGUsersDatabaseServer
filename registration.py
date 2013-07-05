import cgi
import pymysql
import os

#print("Content-Type: text/html")
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
login = form.getvalue('login')
password  = form.getvalue('password')
email = form.getvalue('email')

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
cur.execute("INSERT INTO pgusers(Login,Password,Mail) VALUES (%s,%s,%s)", (login, password, email))
conn.commit()
cur.close()
conn.close()