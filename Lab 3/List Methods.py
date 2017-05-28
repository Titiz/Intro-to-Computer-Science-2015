# List Methods
import logging
arbitrary_list = [1, 'red', 3.1415, [0, 0], 'yellow']

# 1.
arbitrary_list.append(2.718)
print(arbitrary_list)
# 2.
arbitrary_list.insert(5, 2)
print(arbitrary_list)
# 3.
arbitrary_list.remove('red')
print(arbitrary_list)
# 4.
index_31415 = arbitrary_list.index(3.1415)
print(index_31415)
# 5.
try:
    arbitrary_list.sort()
    print(arbitrary_list)
except Exception as ex:
    logging.exception('Caught an error')


# 6.
arbitrary_list.pop(2)
print(arbitrary_list)
# 7.
x = arbitrary_list.copy()
print(x)