from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='sql123$',
                                 host='127.0.0.1',
                                 database='mysql')
cnx.close()
