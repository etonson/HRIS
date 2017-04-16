from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

class HRIS:
    def __init__(self,user,pwd,host,database):
        self.user=user
        self.pwd=pwd
        self.host=host
        self.database=database
        config={'user':self.user,
                'password':self.pwd,
                'host':self.host,
                'database':self.database}
        self.cnx=mysql.connector.connect(**config)
        self.cursor=self.cnx.cursor()

    def INSERT(self,value):
        try:
            string=("insert into employees"
                    "(employeeID,ID,name,email,Phone_number,BirthPlace,Nation,Sex)"
                    "values('%s','%s','%s','%s','%s','%s','%s',%d)")
            self.cursor.execute((string%value))
            self.cnx.commit()
            return 0
        except mysql.connector.IntegrityError as err:
              print("Error: {}".format(err))
              print(err.errno)
              return err.errno
    def DELETE(self,value):
        try:
            string=("DELETE FROM employees"
                    " WHERE employeeID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))

    def UPDATE(self,value):
        try:
            string=("UPDATE employees "
                    "SET employeeID = '%s' ,"
                    "ID = '%s' ,"
                    "name = '%s' ,"
                    "email = '%s' ,"
                    "Phone_number = '%s' ,"
                    "BirthPlace = '%s' ,"
                    "Nation = '%s' ,"
                    "Sex = %d "
                    "WHERE employeeID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))
    def SELECT(self):
        tmp =()
        try:
            string=("select * from employees")
            self.cursor.execute(string)
            return self.cursor
        except mysql.connector.errors.ProgrammingError  as err:
            print("Error: {}".format(err))
class Department(HRIS):
    def __init__(self,user,pwd,host,database):
        super().__init__(user,pwd,host,database)

    def INSERT(self,value):
        try:
            string=("insert into Department"
                    "(DepartmentID,DepartmentTitle,DepartmentManagerID)"
                    "values('%s','%s','%s')")
            self.cursor.execute((string%value))
            self.cnx.commit()
        except mysql.connector.IntegrityError as err:
              print("Error: {}".format(err))

    def DELETE(self,value):
        try:
            string=("DELETE FROM Department"
                    " WHERE DepartmentID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))

    def UPDATE(self,value):
        try:
            string=("UPDATE Department "
                    "SET DepartmentID = '%s' ,"
                    "DepartmentTitle = '%s' ,"
                    "DepartmentManagerID = '%s' "
                    "WHERE DepartmentManagerID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))
        except mysql.connector.errors.IntegrityError as err:
              print("Error: {}".format(err))

class JobBook(HRIS):
    def __init__(self,user,pwd,host,database):
        super().__init__(user,pwd,host,database)

    def INSERT(self,value):
        try:
            string=("insert into JobBook"
                    "(JobBookID,DepartmentID,JobBookLocal)"
                    "values('%s','%s','%s')")
            self.cursor.execute((string%value))
            self.cnx.commit()
        except mysql.connector.IntegrityError as err:
              print("Error: {}".format(err))

    def DELETE(self,value):
        try:
            string=("DELETE FROM JobBook"
                    " WHERE JobBookID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))

    def UPDATE(self,value):
        try:
            string=("UPDATE JobBook "
                    "SET JobBookID = '%s' ,"
                    "DepartmentID = '%s' ,"
                    "JobBookLocal = '%s' "
                    "WHERE JobBookID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))
        except mysql.connector.errors.IntegrityError as err:
            print("Error: {}".format(err))

class JobHistory(HRIS):
    def __init__(self,user,pwd,host,database):
        super().__init__(user,pwd,host,database)

    def INSERT(self,value):
        try:
            string=("insert into JobHistory"
                    "(employeeID,StartDate,OutDate,JobBookID,Class)"
                    "values('%s','%s','%s','%s','%s')")
            self.cursor.execute((string%value))
            self.cnx.commit()
        except mysql.connector.IntegrityError as err:
              print("Error: {}".format(err))

    def DELETE(self,value):
        try:
            string=("DELETE FROM JobHistory"
                    " WHERE employeeID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))

    def UPDATE(self,value):
        try:
            string=("UPDATE JobBook "
                    "SET employeeID = '%s' ,"
                    "StartDate = '%s' ,"
                    "OutDate = '%s' ,"
"JobBookID = '%s' ,"
"Class = '%s' "
                    "WHERE JobBookID = '%s'")
            self.cursor.execute(string%value)
            self.cnx.commit()
        except mysql.connector.errors.ProgrammingError as err:
              print("Error: {}".format(err))
        except mysql.connector.errors.IntegrityError as err:
            print("Error: {}".format(err))
