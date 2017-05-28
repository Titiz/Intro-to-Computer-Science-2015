import sqlite3 as sql
mov = sql.connect('movies.db')
wrld = sql.connect('cia.db')

# Problem set 1, #1 : Find the countries that have exactly four characters



o = wrld.execute('''SELECT name FROM world
 WHERE name LIKE "____"''')

print("Countries with 4 letters:")
while True:
    t_3 = o.fetchone()
    if t_3 == None:
        break

    print(t_3[0])

print('\n')
# Problem set 2, #10
# Show per-capita GDP for the trillion dollar countries to the nearest $1000.

s = wrld.execute('''SELECT name, round(gdp/population, -3) FROM world where gdp > 1000000000000''')
# round(gdp/population, -3) does not seem to round so rounding was done in python.
print('Country : GDP per Capita')
while True:
    t_2 = s.fetchone()
    if t_2 == None:
        break
    print(t_2[0], ':', int(round(t_2[1],-3)))

print('\n')
# Problem Set 7, #8: Show all the cast members of Alien

p = mov.execute('''SELECT name
FROM actor JOIN casting ON actorid=id
WHERE movieid=24
''')

print('Alien cast:')
while True:
    t_1 = p.fetchone()
    if t_1 == None:
        break
    print(t_1[0])

print('\n')


# Actor movie retrieval:
while True:
    movies = []
    a = input('Please input the name of the actor: ')
    if a == '':
        break
    elif len(a.split(' ')) >= 2:
        q = mov.execute('''SELECT DISTINCT title, yr, ord
FROM (movie JOIN casting ON movie.id=movieid) JOIN actor ON actor.id=actorid
WHERE name="{}"
ORDER BY yr'''.format(a))
    while True:
        r = q.fetchone()
        if r == None:
            break
        if r[2] == 1:
            print(r[0]+'*', '-', r[1])
        else:
            print(r[0], '-', r[1])
    print('\n')
