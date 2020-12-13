with open('input', 'r') as fh:
    adps = sorted([
        int(line.strip()) for line in fh.readlines()
    ])


class Tr:

    def __init__(self, t, a, p):
        self.t = t
        self.a = a
        self.p = p

    def valid_path(self):
        if not self.a:
            return self.p
        if max(self.a) < self.t:
            return
        for i, a in enumerate(self.a):
            if a - 3 <= self.t <= a:
                tr = Tr(a, self.a[:i] + self.a[i+1:], self.p + [a])
                p = tr.valid_path()
                if p:
                    return p


p = Tr(0, adps, []).valid_path()
p = [0] + p + [p[-1] + 3]
ds = {}
for i, a in enumerate(p):
    if i + 1 >= len(p):
        break
    d = p[i+1] - a
    if d not in ds:
        ds[d] = 0
    ds[d] += 1

print(ds[1] * ds[3])
