with open('input', 'r') as fh:
    m = [
        line.strip() for line in fh.readlines()
    ]


def look(m, x, y, v):
    i = 0
    dx = x
    dy = y
    while True:
        dx += v[0]
        dy += v[1]
        if dx < 0:
            break
        if dy < 0:
            break
        try:
            c = m[dy][dx]
        except IndexError:
            break
        if c == 'L':
            break
        if c == '#':
            i += 1
            break
    return i


def count(m, x, y):
    return sum([
        look(m, x, y, (-1, 0,)),
        look(m, x, y, (1, 0,)),
        look(m, x, y, (0, -1,)),
        look(m, x, y, (0, 1,)),
        look(m, x, y, (-1, -1,)),
        look(m, x, y, (1, 1,)),
        look(m, x, y, (1, -1,)),
        look(m, x, y, (-1, 1,)),
    ])

la = None
while la != m:
    la = m
    m = []
    for y, r in enumerate(la):
        line = ''
        for x, c in enumerate(r):
            if c == 'L':
                if count(la, x, y) == 0:
                    line += '#'
                    continue
            if c == '#':
                if count(la, x, y) >= 5:
                    line += 'L'
                    continue
            line += c
        m.append(line)

print(
    sum(
        1
        for r in m
        for c in r
        if c == '#'
    )
)
