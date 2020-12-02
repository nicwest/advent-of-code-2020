import re


p = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')

count = 0

with open('input', 'r') as fh:
    for line in fh.readlines():
        l, u, t, s = p.match(line.strip()).groups()
        c = len([c for c in s if c == t])
        if int(l) <= c <= int(u):
            count += 1
print(count)
