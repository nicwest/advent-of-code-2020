with open('input', 'r') as fh:
    # don't need this apparently
    fh.readline()
    raw = [
      n if n == 'x' else int(n)
      for n in fh.readline().strip().split(',')
    ]


ids = []
ts = []
t = 0
for i in raw:
    if i == 'x':
        t += 1
    else:
        ids.append(i)
        ts.append(t)
        t += 1

it = list(zip(ts, ids))
its = sorted(it, key=lambda x: x[1], reverse=True)

t = 0
p = 1
i = 0
while i < len(its):
    o, n = its[i]
    if (t + o) % n == 0:
        i += 1
        p *= n
    else:
        t += p

print(t)
