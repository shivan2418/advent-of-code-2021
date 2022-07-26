import string
from typing import List

small_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

unique_caves = set()
caves = []
cave_dict = {}

class Cave():

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __init__(self,name,small_cave):
        self.name = name
        self.small_cave = small_cave
        self.exits = []

    def valid_exits_from_cave(self) -> List['Cave']:
        return [exit for exit in self.exits if not any([
            self.small_cave and exit.small_cave, exit.name=="start",
        ])]

def parse_input(input):
    lines = input.split()
    for line in lines:
        cave1,cave2 = line.split("-")

        if cave1 not in unique_caves:
            unique_caves.add(cave1)
            caves.append(Cave(cave1,cave1 in string.ascii_lowercase))
        if cave2 not in unique_caves:
            unique_caves.add(cave2)
            caves.append(Cave(cave2,cave2 in string.ascii_lowercase))
    # create a dict for easy name to object lookup
    for c in caves:
        cave_dict[c.name]=c

    # add exits
    for line in lines:
        first_cave, exit = line.split("-")
        cave = cave_dict[first_cave]
        exit_cave = cave_dict[exit]
        if exit not in [c.name for c in cave.exits]:
            cave.exits.append(exit_cave)


if __name__ == '__main__':

    parse_input(small_input)

    origin = cave_dict['start']

    exits = origin.valid_exits_from_cave()
    print(exits)