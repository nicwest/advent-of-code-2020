passports = []
passport = {}

valid = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
]

with open('input', 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            passports.append(passport)
            passport = {}
            continue

        for part in line.split(' '):
            key, value = part.split(':')
            passport[key] = value

    passports.append(passport)

print(
    sum(
        1 for p in passports
        if all(k in p for k in valid)
    )
)
