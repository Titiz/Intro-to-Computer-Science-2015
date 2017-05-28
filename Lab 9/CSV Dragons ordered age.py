# Note that this has been altered from lab 08.
# CSV dragons
# 2.
f = open('dragons.csv')
dragons = []
for i in f:
    dragons.append(i.split(','))
f.close()
ages = {}
ages_l = []
other = {}
dragons.pop(0)
for item in dragons:
    other[item[0]] = [item[1], item[3], item[4]]
for item in dragons:
    if item[2] in ages:
        ages[item[2]].append(item[0])
    else:
        ages[item[2]] = [item[0]]
    if item[2] not in ages_l:
        ages_l.append(item[2])
for i in range(len(ages_l)):
    ages_l[i] = int(ages_l[i])
ages_l.sort()
for i in range(len(ages_l)):
    ages_l[i] = str(ages_l[i])



f = open('dragons.csv', 'w')
f.write('Name,Size,Age,Color,Breed\n')
for i in range(1, len(ages_l)):
    for item in ages[ages_l[i]]:
        f.write(item + ',' + str(other[item][0]) + ',' + str(ages_l[i]) + ',' + str(other[item][1]) + ',' + other[item][2])
f.close()

print('List rearranged and exported!')