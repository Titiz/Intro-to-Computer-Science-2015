__author__ = 'Titas'

url = 'http://www.textfiles.com/etext/FICTION/alice.txt'
import urllib.request
file = urllib.request.urlopen(url)


def count(url, word):
    file = urllib.request.urlopen(url)
    count_alice = 0
    count_lines = 0
    for line in file:
        if line.decode().lower().count(word) > 0:
            count_alice += 1
        count_lines += 1
    return [count_alice, count_lines]

file.close()
print(count(url, 'alice')[0], 'lines out of', count(url, 'alice')[1], "contain the string sequence 'alice'")