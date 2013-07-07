import os
import pymysql
from cgi import parse_qs, escape
class Login:
    def login(self, environ):
        #Global variables
        host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
        user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
        passwd = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
        db = os.environ['OPENSHIFT_APP_NAME']
        # Get data from fields
        parameters = parse_qs(environ.get('QUERY_STRING', ''))
        response_body = ""
        if 'login' in parameters:
                login = escape(parameters['login'][0])
        if 'password' in parameters:
                password = escape(parameters['password'][0])

        #Connect to base
        try:
                conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db)
        except Exception as e:
                s = str(e)
                response_body += s
        cur = conn.cursor()

        cur.execute("SELECT id FROM pgusers where login=%s and password=%s", (login, password))

        id = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        try:
            response_body = str(id[0])
        except Exception as e:
            response_body = str(-1)
        return response_body
