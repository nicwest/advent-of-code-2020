import re


passports = []
passport = {}

req = [
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


valid = 0
for passport in passports:
    if not all(k in passport for k in req):
        continue

    if not (1920 <= int(passport['byr']) <= 2002):
        continue

    if not (2010 <= int(passport['iyr']) <= 2020):
        continue

    if not (2020 <= int(passport['eyr']) <= 2030):
        continue

    hgt = re.match(r'(\d+)(in|cm)', passport['hgt'])
    if not hgt:
        continue

    n, unit = hgt.groups()
    if unit == 'cm' and not (150 <= int(n) <= 193):
        continue

    if unit == 'in' and not (59 <= int(n) <= 76):
        continue

    if not re.match(r'^#[0-9a-f]{6}', passport['hcl']):
        continue

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

    if not re.match(r'^[0-9]{9}$', passport['pid']):
        continue

    valid += 1

print(valid)
