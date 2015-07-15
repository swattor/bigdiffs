#!/usr/bin/python

#http://jessenoller.com/blog/2008/05/30/making-re-creatable-random-data-files-really-fast-in-python
import collections
import os

seed = "1092384956781341341234656953214543219"
#words = open("test_data.txt", "r").read().replace("\n", '').split()
words = open("test_data.txt", "r").read().split()
print words

def fdata():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield '\n'.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)

g = fdata()
size = 1073000 # 1gb
fname = "test.out"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())

