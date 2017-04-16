import mysql.connector

config = {
    'user': 'root',
    'password': 'saxo123',
    'host': '127.0.0.1',
    'database': 'HumanResource',
}

employees = ("CREATE TABLE employees ("
             " employeeID varchar(10) NOT NULL,"
             " ID varchar(20) NOT NULL,"
             " name varchar(7) NOT NULL,"
             " email varchar(30),"
             " Phone_number varchar(15),"
             " BirthPlace varchar(10),"
             " Nation varchar(10),"
             " Sex TINYInt(1),"
             " PRIMARY KEY (employeeID)"
             ") CHARACTER SET utf8 COLLATE utf8_general_ci")
Department =("CREATE TABLE Department ("
             " DepartmentID varchar(5) NOT NULL,"
             " DepartmentTitle varchar(50) NOT NULL, "
             " DepartmentManagerID varchar(10) NOT NULL,"
             " FOREIGN KEY (DepartmentManagerID) REFERENCES employees (employeeID),"
             " PRIMARY KEY (DepartmentID)"
             " )CHARACTER SET utf8 COLLATE utf8_general_ci")
JobBook    =("CREATE TABLE JobBook ("
             " JobBookID varchar(15) NOT NULL,"
             " DepartmentID varchar(25) NOT NULL, "
             " JobBookLocal varchar(65) NOT NULL,"
             " FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID),"
             " PRIMARY KEY (JobBookID)"
             " )CHARACTER SET utf8 COLLATE utf8_general_ci")
JobHistory =("CREATE TABLE JobHistory ("
             " Order int(11) NOT NULL auto_increment,"
             " employeeID varchar(15) NOT NULL,"
             " StartDate DATE NOT NULL, "
             " OutDate DATE NOT NULL, "
             " JobBookID varchar(15) NOT NULL,"
             " Class varchar(3) NOT NULL,"
             " FOREIGN KEY (employeeID) REFERENCES employees (employeeID),"
             " FOREIGN KEY (JobBookID) REFERENCES JobBook (JobBookID)"
             " )CHARACTER SET utf8 COLLATE utf8_general_ci")
PayRoll    =("CREATE TABLE PayRoll ("
             " employeeID varchar(15) NOT NULL,"
             " Post varchar(7) NOT NULL, "
             " PayScale varchar(7) NOT NULL, "
             " FOREIGN KEY (employeeID) REFERENCES employees (employeeID)"
             " )CHARACTER SET utf8 COLLATE utf8_general_ci")
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute(employees)
cursor.execute(Department)
cursor.execute(JobBook)
cursor.execute(JobHistory)
cursor.execute(PayRoll)
cnx.close()
cursor.close()
