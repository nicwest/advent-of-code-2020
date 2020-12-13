with open('input', 'r') as fh:
    numbers = [
        int(line.strip())
        for line in fh.readlines()
    ]


def valid(v, w):
    for i, a in enumerate(w):
        for j, b in enumerate(w):
            if i == j:
                continue
            if a + b == v:
                return True
    return False


c = 25
i = c
while True:
    v = numbers[i]
    w = numbers[i-c:i]
    if valid(v, w):
        i += 1
    else:
        break
print(v)
