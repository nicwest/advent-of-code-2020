with open('input', 'r') as fh:
    count = 0
    group = None
    for line in fh.readlines():
        line = line.strip()
        if group is None:
            group = list(line)
            continue

        if line == '':
            count += len(group)
            group = None
            continue

        group = [c for c in group if c in line]

    count += len(group)
    print(count)
