import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Vivek@123", database="RICITECH")
mycursor = mydb.cursor()
