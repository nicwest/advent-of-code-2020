import itertools
import re

with open('input', 'r') as fh:
    prog = [
        line.strip()
        for line in fh.readlines()
    ]


def masks(m_raw):
    m1 = 0
    mx = []
    for i in range(36):
        c = m_raw[i]
        m1 = m1 << 1
        if c == 'X':
            mx.append(35 - i)
        if c == '1':
            m1 |= 1

    mxs = []
    x = m1
    mxs.append(x)
    return m1, mx


pat = re.compile(r'^(mem|mask)(\[(\d+)\])? = (.*)$')

mem = {}
m1 = 0
m0 = 0
mx = []
for line in prog:
    cmd, _, on, d = pat.match(line).groups()
    if cmd == 'mask':
        m1, mx = masks(d)
    else:
        n = int(on) | m1
        for p in itertools.product([1, 0], repeat=len(mx)):
            for i, bit in enumerate(mx):
                if p[i]:
                    n |= (1 << bit)
                else:
                    n &= ~(1 << bit)
            mem[n] = int(d)

print(sum(mem.values()))
