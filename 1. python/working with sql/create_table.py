import mysql.connector
mydb= mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = 'password'
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute('create database if not exists test1')
mycursor.execute('CREATE TABLE if not exists test1.test1(c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))')
mycursor.execute("INSERT INTO test1.test1 VALUES(1,'jas',2,3.0,'ansh')")
mydb.close()