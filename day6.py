from collections import Counter, defaultdict

import tqdm
from functools import lru_cache
test_input = [3,4,3,1,2]
input = [4,1,4,1,3,3,1,4,3,3,2,1,1,3,5,1,3,5,2,5,1,5,5,1,3,2,5,3,1,3,4,2,3,2,3,3,2,1,5,4,1,1,1,2,1,4,4,4,2,1,2,1,5,1,5,1,2,1,4,4,5,3,3,4,1,4,4,2,1,4,4,3,5,2,5,4,1,5,1,1,1,4,5,3,4,3,4,2,2,2,2,4,5,3,5,2,4,2,3,4,1,4,4,1,4,5,3,4,2,2,2,4,3,3,3,3,4,2,1,2,5,5,3,2,3,5,5,5,4,4,5,5,4,3,4,1,5,1,3,4,4,1,3,1,3,1,1,2,4,5,3,1,2,4,3,3,5,4,4,5,4,1,3,1,1,4,4,4,4,3,4,3,1,4,5,1,2,4,3,5,1,1,2,1,1,5,4,2,1,5,4,5,2,4,4,1,5,2,2,5,3,3,2,3,1,5,5,5,4,3,1,1,5,1,4,5,2,1,3,1,2,4,4,1,1,2,5,3,1,5,2,4,5,1,2,3,1,2,2,1,2,2,1,4,1,3,4,2,1,1,5,4,1,5,4,4,3,1,3,3,1,1,3,3,4,2,3,4,2,3,1,4,1,5,3,1,1,5,3,2,3,5,1,3,1,1,3,5,1,5,1,1,3,1,1,1,1,3,3,1]

class Laternfish:

    fish = []
    new_fish = []

    def __init__(self,timer):
        self.timer = timer

    def __str__(self):
        return f"{self.timer}"

    def __repr__(self):
        return f"{self.timer}"

    @lru_cache(maxsize=8)
    def update(self,timer):
        if timer==0:
            Laternfish.new_fish.append(Laternfish(8))
            self.reset()
        else:
            self.timer = timer-1

    def reset(self):
        self.timer = 6


def simulate_fish(input,days):

    Laternfish.fish = [Laternfish(n) for n in input]


    with tqdm.tqdm(total=days,desc="Simulating fish") as bar:
        for _ in range(days):
            for f in Laternfish.fish:
                f.update(f.timer)
            Laternfish.fish.extend(Laternfish.new_fish)
            Laternfish.new_fish = []
            bar.update()

    print(len(Laternfish.fish))

def simulate_fish_large_number(input,days):

    fish = [n for n in input]

    fish_counter = dict(Counter(fish))
    fish_counter[0] = 0

    for _ in range(days):
        # all timer 0 fish reset to 6 and spawn a timer 8 timer later

        fish_counter_new = defaultdict(int,{key-1:value for key,value in fish_counter.items() if key !=0})

        try:
            fish_counter_new[8] += fish_counter[0]
            fish_counter_new[6] += fish_counter[0]
        except KeyError:
            pass

        fish_counter = fish_counter_new

    print(sum(fish_counter.values()))

if __name__ == '__main__':
    simulate_fish_large_number(test_input,18)
    simulate_fish_large_number(input,80)
    simulate_fish_large_number(input,256)
