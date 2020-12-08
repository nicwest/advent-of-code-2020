import re


bags = {}
BAG_PATTERN = re.compile(r'(\d+)? ?(\w+ \w+) bags?')


class Bag:

    def __init__(self, name):
        self.name = name
        self.contained_in = []
        self.contains = []
        self.counted = False

    def add(self, bag, n):
        self.contains.append((n, bag, ))
        bag.contained_in.append(self)

    def how_many_contain(self):
        self.counted = True
        return sum(
            1 + bag.how_many_contain()
            for bag in self.contained_in
            if not bag.counted
        )

    def contains_how_many(self):
        return sum(
            n + (n * bag.contains_how_many())
            for n, bag in self.contains
        )

    def __repr__(self):
        return f'<Bag: {self.name}>'


with open('input', 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        container = None
        for match in BAG_PATTERN.finditer(line):
            n, name = match.groups()

            if name == 'no other':
                continue

            if name not in bags:
                bags[name] = Bag(name)

            bag = bags[name]

            if not container:
                container = bag
            else:
                container.add(bag, int(n))

print(bags['shiny gold'].how_many_contain())
print(bags['shiny gold'].contains_how_many())
