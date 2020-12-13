with open('input', 'r') as fh:
    inst = [
        (line.strip()[0], int(line.strip()[1:]), )
        for line in fh.readlines()
    ]


x = 0
y = 0
d = (1, 0)
for a, v in inst:
    if a == 'F':
        x += v * d[0]
        y += v * d[1]
    if a == 'N':
        y -= v
    if a == 'E':
        x += v
    if a == 'S':
        y += v
    if a == 'W':
        x -= v
    if a == 'L':
        # clockwise
        while v > 0:
            d = (d[1], -d[0],)
            v -= 90
    if a == 'R':
        # anti-clockwise
        while v > 0:
            d = (-d[1], d[0], )
            v -= 90

print(abs(x) + abs(y))
