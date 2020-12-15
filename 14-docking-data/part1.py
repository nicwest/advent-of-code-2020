import re


with open('test2', 'r') as fh:
    prog = [
        line.strip()
        for line in fh.readlines()
    ]


def masks(m_raw):
    m_1 = '0b'
    m_0 = '0b'
    for i in range(36):
        c = m_raw[i]
        if c == 'X':
            m_1 += '0'
            m_0 += '1'
        else:
            m_1 += c
            m_0 += c
    return eval(m_1), eval(m_0)


pat = re.compile(r'^(mem|mask)(\[(\d+)\])? = (.*)$')

mem = {}
m_1 = 0
m_0 = 0
for line in prog:
    cmd, _, n, d = pat.match(line).groups()
    if cmd == 'mask':
        m_1, m_0 = masks(d)
    else:
        d = int(d) | m_1
        d = d & m_0
        mem[int(n)] = d

print(sum(mem.values()))
