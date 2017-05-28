# Note that this has been altered from lab 08.
# CSV dragons
# 1.
f = open('dragons.csv')
dragons = []
for i in f:
    dragons.append(i.split(','))
f.close()
age_size_color = {}
breeds = {}
dragons.pop(0)
for i in range(len(dragons)):
    if dragons[i][4] in breeds:
        breeds[dragons[i][4]].append(dragons[i][0])
    else:
        breeds[dragons[i][4]] = [dragons[i][0]]
    age_size_color[dragons[i][0]] = [dragons[i][1], dragons[i][2], dragons[i][3]]

breed_list = list(breeds.keys())
breed_list.sort()
breed_d = []
for item in breed_list:
    breed_d.append(breeds[item])

for i in range(len(breed_d)):
    breed_d[i].sort()


for i in range(len(breed_list)):
    breeds[breed_list[i].strip()] = breed_d[i]
f = open('dragons.csv', 'w')
f.write('Name,Size,Age,Color,Breed\n')
for i in range(len(breed_list)):
    for item in breed_d[i]:
        f.write(item + ',' + str(age_size_color[item][0]) + ',' + str(age_size_color[item][1]) + ',' + str(age_size_color[item][2]) + ',' + breed_list[i])
f.close()
print('List rearranged and exported!')
