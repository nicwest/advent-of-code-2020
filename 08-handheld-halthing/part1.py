with open('input', 'r') as fh:
    prog = [
        (line[:3], int(line[4:]), )
        for line in fh.readlines()
    ]

acc = 0
i = 0
e = []

while True:
    op, arg = prog[i]
    if i in e:
        print(acc)
        break
    e.append(i)
    if op == 'acc':
        acc += arg
        i += 1
    elif op == 'jmp':
        i += arg
    elif op == 'nop':
        i += 1
