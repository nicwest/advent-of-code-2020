with open('input', 'r') as fh:
    t = int(fh.readline().strip())
    ids = [
        int(n)
        for n in fh.readline().strip().split(',')
        if n != 'x'
    ]

ot = t
go = 1
while go:
    for i in ids:
        if t % i == 0:
            print((t - ot) * i)
            go = 0
    t += 1
