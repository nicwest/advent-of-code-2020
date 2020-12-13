with open('input', 'r') as fh:
    m = [
       line.strip()
       for line in fh.readlines()
    ]


def surround(m, x, y):
    ly = len(m) 
    lx = len(m[0])
    d = [
        (-1, -1,),
        (-1, 0,),
        (-1, 1,),
        (0, 1,),
        (1, 1,),
        (1, 0,),
        (1, -1,),
        (0, -1,),
    ]
    return [
        m[y+dy][x+dx]
        for dx, dy in d
        if -1 < (x + dx) < lx and -1 < (y + dy) < ly
    ]


last = None
while m != last:
    last = m
    m = []
    for y, r in enumerate(last):
        line = ''
        for x, c in enumerate(r):
            if c == 'L':
                if not any(s == '#' for s in surround(last, x, y)):
                    line += '#'
                    continue
            if c == '#':
                if sum(1 for s in surround(last, x, y) if s == '#') >= 4:
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
