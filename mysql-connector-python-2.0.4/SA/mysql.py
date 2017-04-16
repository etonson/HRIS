import sys
sys.path.append('/usr/lib/python3/dist-packages')
from mysql.connector import *

config = {
    'user': 'root',
    'password': 'saxo123',
    'host': '127.0.0.1',
    'database': 'HumanSourece',
}

cnx = mysql.connector.connect(**config)
HumanData = ("CREATE TABLE `HumanData` ("
             " 'StaffCode' varchar(50) NOT NULL,"
             " `id' varchar(50) NOT NULL,"
             " `name` varchar(50) NOT NULL,"
             " `Grade` int NOT NULL,"
             " PRIMARY KEY (`StaffCode`)"
             ") "
             )
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute(HumanData)
cnx.close()
cursor.close()
