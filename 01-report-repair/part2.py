import sys


with open('input', 'r') as fh:
    ns = sorted([int(line.strip()) for line in fh.readlines()])

for n in ns:
    for n2 in ns:
        for n3 in ns:
            if n + n2 + n3 == 2020:
                print(n*n2*n3)
                sys.exit()
