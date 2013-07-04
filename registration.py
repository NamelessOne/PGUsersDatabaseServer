import cgi
import pymysql

#print("Content-Type: text/html")
# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
login = form.getvalue('login')
password  = form.getvalue('password')
email = form.getvalue('email')

#Работа с базой
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='pen3souin', db='paintinggamedb')
cur = conn.cursor()
#TODO сделать отлов ошибок MySQL, например на уникальность логина/мыла и т.п
cur.execute("INSERT INTO pgusers(Login,Password,Mail) VALUES (%s,%s,%s)", (login, password, email))
conn.commit()
cur.close()
conn.close()