def calc(inp):
    i = 0
    u = 127
    row = 0
    col = 0
    while i < 7:
        d = (u - row) // 2
        if inp[i] == 'F':
            u -= d + 1
        else:
            row += d + 1
        i += 1

    u = 7
    while i < 10:
        d = (u - col) // 2
        if inp[i] == 'L':
            u -= d + 1
        else:
            col += d + 1
        i += 1

    return row, col, ((row * 8) + col)


assert calc('FBFBBFFRLR') == (44, 5, 357)
assert calc('BFFFBBFRRR') == (70, 7, 567)
assert calc('FFFBBBFRRR') == (14, 7, 119)
assert calc('BBFFBBFRLL') == (102, 4, 820)


with open('input', 'r') as fh:
    m = 0
    first = 0
    second = 0
    ids = []
    for line in fh.readlines():
        _, _, id = calc(line.strip())
        ids.append(id)

    ids.sort()

    for i, id in enumerate(ids):
        if i + 1 == len(ids):
            break
        if id + 2 == ids[i + 1]:
            print(id + 1)
