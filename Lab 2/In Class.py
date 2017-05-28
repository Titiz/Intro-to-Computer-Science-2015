import logging
# In class

x = "Mary had a little lamb"

print(x[-5:-1:2])
print(x[8:4:-2])

y = '0123456789'

print(y[8:2:-2])
print(y[8:-8:-2])
print(y[-2:-8:-2])

# Lists

x_list = [1, 2, 3]
y_list = [4, 5, 6]

print(x_list + y_list)

a_list = [1, 'This', 12.1]
word = 'ello world'

try:
    a_list[0] = 'H'
    word[0] = 'Hello world'

except Exception as ex:
    logging.exception('Caught an error')
    word = 'H' + word[0:]


print(word)
print(a_list)
