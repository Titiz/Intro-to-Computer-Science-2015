import pymysql as sql

conn = sql.connect(host='10.224.41.239',
                       user = 'cs101',
                       db = 'twitter',
                       autocommit = True)

curr = conn.cursor()

a = curr.execute("SELECT * FROM tweet")

while True:




