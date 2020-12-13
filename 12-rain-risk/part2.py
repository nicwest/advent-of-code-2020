with open('input', 'r') as fh:
    inst = [
        (line.strip()[0], int(line.strip()[1:]), )
        for line in fh.readlines()
    ]

x = 0
y = 0
w = (10, -1,)

for a, v in inst:
    if a == 'F':
        x += v * w[0]
        y += v * w[1]
    if a == 'N':
        w = (w[0], w[1] - v,)
    if a == 'E':
        w = (w[0] + v, w[1],)
    if a == 'S':
        w = (w[0], w[1] + v,)
    if a == 'W':
        w = (w[0] - v, w[1],)
    if a == 'L':
        # clockwise
        while v > 0:
            w = (w[1], -w[0],)
            v -= 90
    if a == 'R':
        # anti-clockwise
        while v > 0:
            w = (-w[1], w[0], )
            v -= 90


print(abs(x) + abs(y))
