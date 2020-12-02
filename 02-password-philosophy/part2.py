import re


p = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')

count = 0

with open('input', 'r') as fh:
    for line in fh.readlines():
        l, u, t, s = p.match(line.strip()).groups()
        cs = [s[int(l) - 1], s[int(u) - 1]]
        if sum([1 for c in cs if c == t]) == 1:
            count += 1
print(count)
