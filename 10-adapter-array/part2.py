class Adapter:

    def __init__(self, v):
        self.v = v

    def ways_to_here(self, other, done):
        if self.v in done:
            return done[self.v]
        w = 0
        for i, a in enumerate(other):
            if self.v - 3 <= a.v < self.v:
                o = other[:i]
                w += max(1, a.ways_to_here(o, done))
        done[self.v] = w
        return w

    def __repr__(self):
        return f'{self.v}'


with open('input', 'r') as fh:
    adps = sorted([0] + [
        int(line.strip()) for line in fh.readlines()
    ])
    adps = list(map(lambda x: Adapter(x), adps))

print(adps[-1].ways_to_here(adps, {}))
