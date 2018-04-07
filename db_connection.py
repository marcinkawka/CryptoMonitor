#!/usr/bin/python3.5
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='crypto' host='10.25.25.1' password='Azsxqwe!23'")
except:
    print("I am unable to connect to the database")


cur = conn.cursor()
try:
	cur.execute("Insert into crypto_db.tickers(type_id,stock_id,buy,sell,ts) values(0,0,\'0\',\'0\',CURRENT_TIMESTAMP) ") 
	conn.commit()
except Exception as e: 
	print("Cannot Insert "+e)

cur.close()
conn.close()