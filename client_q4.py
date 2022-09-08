import rpyc
import sys
import os

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
c = rpyc.connect(server,18861)

n = int(sys.argv[2])
list = []
for i in range(n):
    list.append(i)

print(c.root.soma_lista(list))
