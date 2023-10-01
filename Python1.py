
import mysql.connector

mydb = my.sql.connector.connect(
    host="localhost",
    user ="root",
    passwd ="123password")



#Create DataBase

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testdb")

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)


mycursor.execute("CREATE TABLE students(
                 name VARCHAR(255), age INTEGER(10)
)")

mycursor.execute("SHOW TABLE")

for db in mycursor:
    print(db)




# Populate the columns in values


sqlFormula ="INSERT INTO students (name, age) VALUES (%s, %s)" # Insert Columns


students= [("BOB", 22), ("JACK", 66)]
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1) # Insert data

mycursor.executemany(sqlFormula, students)


mydb.commit() # Saves the change



# SELECT DATA

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for row in my results:
print row


mycursor.execute("SELECT age, name FROM students")

myresult = mycursor.fetchall() # returns eveything from results
myresult = mycursor.fetchone() # returns the first row from the result


for row in my results:
print row



sql = "Select * from students WHERE name = '%s"

mycursor.execute(sql, "Mike")


results = mycursor.fetchall()

for i in results:
    print(i)



# Updating a key in the database

mycursor = mydb.cursor()


sql = UPDATE students SET age = 13 where name ="Bob"

mycursor.execute(sql)

mydb.commit()