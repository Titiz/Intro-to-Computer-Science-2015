import pymysql as sql
import sqlite3 as db
#
# TODO: establish a connection and create a cursor
#

#conn = sql.connect(host='10.224.41.239',
 #                      user = 'cs101',
    #                   db = 'twitter',
     #                  autocommit = True)

# SQLite version:

conn = db.connect('twitter.db')
curr = conn.cursor()

opts = [
    'Tweet!',
    'Show tweets',
    'List users',
    'Show tweets from user',
    'Like',
    'Quit'
]
user = input('Please enter your username: ')
while True:
    for (i, j) in enumerate(opts):
        print('  ', i + 1, j)
    choice = int(input('Please enter your choice: '))

    if choice == 1:
        message = input('Tweet: ')[:140]
        #
        # TODO: Add t to the database for this user. Your insert
        #       statement only needs to include the user and the
        #       message
        #
        curr.execute('''INSERT INTO tweet (user, message) VALUES ("{}","{}")'''.format(user, message))
        conn.commit()
    elif choice == 2:
        #
        # TODO: Display all of the tweets (all of the information
        #       really) from the database. Order by message timestamps
        #
        msgs = curr.execute('''SELECT id, user, message, likes, tstamp FROM tweet ORDER BY tstamp DESC''')
        count = 0
        while True:
            x = msgs.fetchone()
            if count == 10 or x == None:
                break
            print("'" + x[2] + "'", 'at', x[4], 'by', x[1] + '.', 'Likes:', x[3], 'ID:', x[0])
            count += 1


    elif choice == 3:
        #
        # TODO: Display all users in the database. Order by user name
        #
        msgs = curr.execute('''SELECT DISTINCT user
FROM tweet
ORDER BY user''')

        while True:
            x = msgs.fetchone()
            if x == None:
                break
            print(x[0])
    elif choice == 4:
        u = input('User: ')
        #
        # TODO: Display all of the tweets (all of the information
        #       really) from the database for a specified user. Order
        #       by message timestamps
        #

        msgs = curr.execute('''SELECT id, user, message, likes, tstamp
FROM tweet
WHERE user = '{}'
ORDER BY tstamp DESC'''.format(u))
        while True:
            x = msgs.fetchone()
            if x == None:
                break
            print("'" + x[2] + "'", 'at', x[4], 'by', x[1] + '.', 'Likes:', x[3], 'ID:', x[0])

        
    elif choice == 5:
        tweet = input('Which tweet: ')
        #
        # TODO: Update the like attribute for the specified tweet
        #       id. Your update statement should, literally, set likes
        #       to likes + 1
        #

        msgs = curr.execute('''UPDATE tweet
SET likes = likes + 1
WHERE id = {}'''.format(int(tweet)))
        conn.commit()
    elif choice == 6:
        #
        # TODO: quit the program. Remember to close the cursor and the
        #       connection
        #

        curr.close()
        conn.close()
        break

    print()
