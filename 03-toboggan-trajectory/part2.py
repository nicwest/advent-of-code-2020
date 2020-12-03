import math


with open('input', 'r') as fh:
    the_map = [line.strip() for line in fh.readlines()]

ds = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


mx = len(the_map[0])
my = len(the_map)


def count_trees(dx, dy):
    x = 0
    y = 0
    trees = 0

    while y < my:
        if x >= mx:
            x -= mx
        if the_map[y][x] == '#':
            trees += 1
        x += dx
        y += dy
    return trees


print(math.prod(count_trees(*d) for d in ds))
