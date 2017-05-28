# CSV dragons
# 3.
f = open('dragons.csv')
dragons = []
for i in f:
    dragons.append(i.split(','))
f.close()
age_size_color = {}
breeds = {}
dragons.pop(0)


sizes = {}
names = {}
for item in dragons:
    if item[4] in sizes.keys():
        sizes[item[4]].append(int(item[1]))
        names[item[4]].append(item[0])
    else:
        sizes[item[4]] = [int(item[1])]
        names[item[4]] = [item[0]]


biggest = {}
name = {}
for i in sizes.keys():
    maximum = max(sizes[i])
    for j in range(len(sizes[i])):
        if int(sizes[i][j]) == maximum:
            if i in biggest.keys():
                biggest[i].append(sizes[i][j])
                name[i].append(names[i])
            else:
                biggest[i] = [sizes[i][j]]
                name[i] = [names[i]]


for item in biggest:
    string = ''
    print('\nLARGEST', item[:-1], 'dragons:')
    for i in name[item][0]:
        string += i + ', '
    print(string)