# 2.
shift = 17
f = open('original.txt')
lines = []
for i in f:
    lines.append(i)
print(lines)
f.close
for i in range(len(lines)):
    string = ''
    for letter in lines[i]:
        if ord(letter) not in range(97, 123):
            string += letter
        else:
            if ord(letter)+17 > 122:
                string += chr(97 + ((ord(letter)+17) - 123))
            else:
                string += chr(ord(letter) + 17)

    lines[i] = string




print(lines)

f = open('encrypted.txt', 'w')
for item in lines:
    f.write(item)

f.close()
lines_r = []
f = open('encrypted.txt', 'r')
for i in f:
    lines_r.append(i)
f.close
for i in range(len(lines_r)):
    string = ''
    for letter in lines_r[i]:
        if ord(letter) not in range(97, 123):
            string += letter
        else:
            if ord(letter)-17 < 97:
                string += chr(123 -(97 - (ord(letter) - 17)))
            else:
                string += chr(ord(letter) - 17)

    lines_r[i] = string
print(lines_r)
f = open('unencrypted.txt', 'w')
for line in lines_r:
    f.write(line)
f.close()

print('\nfilecmp yields the following:')
import filecmp
diff = filecmp.cmp('original.txt', 'unencrypted.txt', False) # Returns false, even though the content is exactly the same.
print(diff)

print('\nA line by line comparison yields the following:')


f = open('unencrypted.txt', 'r')
s = open('original.txt', 'r')
count = 0
for line in f:
    count += 1
    if line == s.readline():
        print('Line', count, 'is the same in both files -', True)
    else:
        print('Line', count, 'is the same in both files -', False)

print('\nOn my end, filecmp shows that the files are not the same, whereas '
      'the line by line test shows all lines to be the same.')