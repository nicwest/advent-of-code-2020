with open('input', 'r') as fh:
    the_map = [line.strip() for line in fh.readlines()]

mx = len(the_map[0])
my = len(the_map)
dx = 3
dy = 1
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

print(trees)
