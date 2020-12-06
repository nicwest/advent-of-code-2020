with open('input', 'r') as fh:
    groups = []
    group = set()
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            groups.append(group)
            group = set()
            continue

        for c in line:
            group.add(c)
    groups.append(group)

    print(sum(len(group) for group in groups))
