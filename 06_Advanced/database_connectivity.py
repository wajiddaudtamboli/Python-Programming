# database connectivity

#1 creating table
'''
import sqlite3
con=sqlite3.connect('test.db')
con.execute("create table emp(empid INTEGER(20),name TEXT(20))")
'''

#2 inserting a data into table
import sqlite3
con=sqlite3.connect('test.db')

sql=("insert into emp(empid,name) values(101,'tabassum')")
con.execute(sql)
con.commit()

