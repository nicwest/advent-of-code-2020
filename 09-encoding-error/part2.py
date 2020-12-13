with open('input', 'r') as fh:
    numbers = [
        int(line.strip())
        for line in fh.readlines()
    ]

t = 375054920
i = 0
w = []
v = 0
o = 1

while v != t:
    o += 1
    if o > len(numbers):
        i += 1
        o = 1
    w = numbers[i:i+o]
    v = sum(w)

print(min(w) + max(w))
