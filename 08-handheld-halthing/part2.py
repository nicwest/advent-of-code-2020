with open('input', 'r') as fh:
    prog = [
        (line[:3], int(line[4:]), )
        for line in fh.readlines()
    ]


def fiddle(n):
    acc = 0
    i = 0
    e = []

    while i < len(prog):
        op, arg = prog[i]
        if i in e:
            return False
        if i == n:
            if op == 'nop':
                op = 'jmp'
            if op == 'jmp':
                op = 'nop'

        e.append(i)
        if op == 'acc':
            acc += arg
            i += 1
        elif op == 'jmp':
            i += arg
        elif op == 'nop':
            i += 1
    return acc


for i in range(len(prog)):
    r = fiddle(i)
    if r:
        print(i, r)
