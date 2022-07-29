import copy
import random
import string
from typing import List
from collections import Counter

ten_cave = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

nineteen_cave = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

nineteen_cave_result = set("""start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end""".split('\n'))

medium_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

small_input_result = """start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end"""

input = """re-js
qx-CG
start-js
start-bj
qx-ak
js-bj
ak-re
CG-ak
js-CG
bj-re
ak-lg
lg-CG
qx-re
WP-ak
WP-end
re-lg
end-ak
WP-re
bj-CG
qx-start
bj-WP
JG-lg
end-lg
lg-iw"""

unique_caves = set()
caves = []
cave_dict = {}


class Cave(object):

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __init__(self, name, small_cave):
        self.name = name
        self.small_cave = small_cave
        self.exits = set()

    def valid_exits_from_cave(self, previous_steps=None) -> List['Cave']:
        """Valid exits when can visit each cave once"""
        valid_caves = [exit for exit in self.exits if not any([exit.name=="start", exit.small_cave and exit.name in previous_steps])]
        if previous_steps is not None:
            small_caves_visited = [c for c in previous_steps if is_small_cave(c)]
            valid_caves = [c for c in valid_caves if c.name not in small_caves_visited]

        return sorted(valid_caves, key=lambda c: c.name)

    def valid_exits_from_cave_visit_one_cave_twice(self,previous_steps=None,cave_visited_twice=None) -> List['Cave']:
        """Valid exits when can visit one cave twice"""

        cave_visit_counter = Counter([step for step in previous_steps if self.all_lower(step)])

        cave_name, count = cave_visit_counter.most_common(1)[0]

        valid_caves = [exit for exit in self.exits if exit.name!="start"]

        if previous_steps is not None:
            small_caves_visited = [c for c in previous_steps if is_small_cave(c)]
            if count >= 2:
                valid_caves = [exit for exit in valid_caves if not any([exit.small_cave and exit.name in previous_steps])]
                valid_caves = [c for c in valid_caves if c.name not in small_caves_visited]

        return sorted(valid_caves, key=lambda c: c.name)


    @staticmethod
    def all_lower(string) -> bool:
        return all([s.islower() for s in string])

    paths_traveled: List[List[str]] = []

def is_small_cave(string: str):
    return string not in ['start', 'end'] and all([s.islower() for s in string])

def parse_input(input):
    lines = input.split()
    for line in lines:
        cave1, cave2 = line.split("-")

        if cave1 not in unique_caves:
            unique_caves.add(cave1)
            caves.append(Cave(cave1, is_small_cave(cave1)))
        if cave2 not in unique_caves:
            unique_caves.add(cave2)
            caves.append(Cave(cave2, is_small_cave(cave2)))
    # create a dict for easy name to object lookup
    for c in caves:
        cave_dict[c.name] = c

    # add exits
    for line in lines:
        first_cave_name, second_cave_name = line.split("-")

        first_cave = cave_dict[first_cave_name]
        second_cave = cave_dict[second_cave_name]

        first_cave.exits.add(second_cave)
        second_cave.exits.add(first_cave)


def map_path_from_location(start_cave, previous_steps):
    exits = start_cave.valid_exits_from_cave(previous_steps)

    for e in exits:
        if e.name == 'end':
            path = previous_steps + ['end']
            Cave.paths_traveled.append(path)
        else:
            map_path_from_location(e, previous_steps + [e.name])

def map_from_location_with_queue(start_cave: Cave, previous_steps):
    exits = start_cave.valid_exits_from_cave_visit_one_cave_twice(previous_steps)

    for e in exits:
        if e.name == 'end':
            path = previous_steps + ['end']
            Cave.paths_traveled.append(path)
        else:
            map_from_location_with_queue(e, previous_steps + [e.name])


def deduplicate(paths_traveled:List[List[str]]):

    result = set()
    for path in paths_traveled:
        result.add(",".join(path))

    return result

def solve_part_1():
    # setup
    parse_input(input)
    Cave.paths_traveled = []

    # set start location
    present_cave = cave_dict['start']
    map_path_from_location(present_cave, ['start'])

    result = deduplicate(Cave.paths_traveled)

    print(len(result))

def solve_part_2(input):
    # setup
    parse_input(input)
    Cave.paths_traveled = []

    # set start location
    present_cave = cave_dict['start']
    map_from_location_with_queue(present_cave, ['start'])


    for c in Cave.paths_traveled:
        print(c)

    print(len(Cave.paths_traveled))

if __name__ == '__main__':

    #solve_part_1()
    solve_part_2(input)