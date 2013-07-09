import os
import pymysql
from pymysql import err
from cgi import parse_qs, escape
class Registration:
    def register(self, environ):
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
        if 'email' in parameters:
                email = escape(parameters['email'][0])

        #Connect to base
        try:
                conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db)
        except Exception as e:
            s = str(e)
            response_body += s
        cur = conn.cursor()
        try:
                cur.execute("INSERT INTO pgusers(Login,Password,Mail) VALUES (%s,%s,%s)", (login, password, email))
        except pymysql.DataError as e:
            #Ошибки MySQL всегда четырехразрядные, помни об этом!!!
            s = str(e.args[0])
            response_body +=  "-" + s[1] + s[2] + s[3] + s[4]
        except pymysql.IntegrityError as e:
            s = str(e.args[0])
            response_body +=  "-" + s[1] + s[2] + s[3] + s[4]
        except pymysql.ProgrammingError as e:
            s = str(e.args[0])
            response_body +=  "-" + s[1] + s[2] + s[3] + s[4]
        except pymysql.NotSupportedError as e:
            s = str(e.args[0])
            response_body +=  "-" + s[1] + s[2] + s[3] + s[4]
        conn.commit()
        cur.close()
        conn.close()

        return response_body