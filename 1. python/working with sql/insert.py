import mysql.connector
mydb= mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = 'password'
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO test.test1 VALUES(1,'jas',2,3.0,'ansh')")
mydb.commit()
mydb.close()