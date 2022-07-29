using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_11 {

    class Octupus {

        public static int flash_count = 0;
        public static List<Octupus> octupus_population = new List<Octupus>();

        public static Dictionary<Tuple<int, int>, Octupus> octupus_dict = new Dictionary<Tuple<int, int>, Octupus>();

        public Tuple<int, int> location;
        public int energy_level;
        public bool flashed_this_cycle = false;

        public static void increaseEnergyOffAll() {
            Octupus.octupus_dict.Values.ToList().ForEach(oc => oc.increase_energy());
        }

        public static void resetFlashedOctopi() {
            Octupus.octupus_dict.Values.Where(oc => oc.flashed_this_cycle).ToList().ForEach(oc => {
                oc.reset_energy();
                oc.flashed_this_cycle = false;
            });
        }

        public Octupus(Tuple<int, int> location, int energy_level) {
            this.location = location;
            this.energy_level = energy_level;
        }

        public void flash() {
            if (!this.flashed_this_cycle) {
                this.flashed_this_cycle = true;
                Octupus.flash_count++;
                this.increase_adjacent_energy();
            }
        }

        public void increase_energy() {
            this.energy_level++;

            if (this.energy_level > 9 && !this.flashed_this_cycle) {
                this.flash();
            }

        }

        public void reset_energy() {
            this.energy_level = 0;
        }

        public void increase_adjacent_energy() {
            var adjacent = this.getAdjacentOptopi();
            adjacent.ForEach(oc => {
                oc.increase_energy();
            });
        }

        public List<Octupus> getAdjacentOptopi() {

            int[] xs = { -1, 0, 1 };
            int[] ys = { -1, 0, 1 };

            List<Tuple<int, int>> coordinates = new List<Tuple<int, int>>();

            List<Octupus> adjacent_octopi = new List<Octupus>();

            foreach (int x in xs) {
                foreach (int y in ys) {
                    coordinates.Add(new Tuple<int, int>(this.location.Item1 + x, this.location.Item2 + y));
                }
            }
            // remove your own coordiante
            coordinates.Remove(this.location);

            Octupus value;

            coordinates.ForEach(cor => {
                if (Octupus.octupus_dict.TryGetValue(cor, out value)) {
                    adjacent_octopi.Add(value);
                }
            });

            return adjacent_octopi;


        }
    }

    internal class Day11 {

        public static void createOctopi(string input) {

            var cleaned_input = input.Split('\r').Select(s => s.Replace('\n'.ToString(), String.Empty));

            int x = 0;
            int y = 0;
            int num_created = 0;

            foreach (string str in cleaned_input) {
                foreach (char c in str) {
                    var location = new Tuple<int, int>(x, y);
                    var new_octopi = new Octupus(location, int.Parse(c.ToString()));
                    Octupus.octupus_dict.Add(new Tuple<int, int>(x, y), new_octopi);
                    x++;
                    num_created++;
                }
                y++;
                x = 0;
            }

        }

        private static void doStep() {
            Octupus.increaseEnergyOffAll();
            var just_reached_critical_energy = Octupus.octupus_dict.Values.Where<Octupus>(oc => oc.energy_level > 9).ToList();
            just_reached_critical_energy.ForEach(oc => oc.flash());
            Octupus.resetFlashedOctopi();
        }

        private static void doStep2() {
            Octupus.increaseEnergyOffAll();

            var just_reached_critical_energy = Octupus.octupus_dict.Values.Where<Octupus>(oc => oc.energy_level > 9).ToList();

            just_reached_critical_energy.ForEach(oc => oc.flash());


        }

        public static int SolvePart1(string input) {

            createOctopi(input);

            for (int i = 0; i < 100; i++) {
                doStep();
            }
            Console.Write($"Total flashes test input {Octupus.flash_count}");
            return Octupus.flash_count;
        }

        public static void SolvePart2(string input) {
            createOctopi(input);

            double round = 0;
            while (true) {
                Console.WriteLine($"Round: {round}");
                Octupus.increaseEnergyOffAll();
                var just_reached_critical_energy = Octupus.octupus_dict.Values.Where<Octupus>(oc => oc.energy_level > 9).ToList();

                just_reached_critical_energy.ForEach(oc => oc.flash());

                if (Octupus.octupus_dict.Values.All(oc => oc.flashed_this_cycle)) {
                    Console.WriteLine($"ALL SYNCED {round}");
                    break;
                }

                Octupus.resetFlashedOctopi();

                round++;
            }


        }

        static void Main(string[] args) {

            string test_input = @"5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526";

            string input = @"5212166716
1567322581
2268461548
3481561744
6248342248
6526667368
5627335775
8124511754
4614137683
4724561156";

            //int test_result = Solve(test_input);
            //Debug.Assert(test_result == 1656);

            //Octupus.octupus_dict.Clear();

            //int result = SolvePart1(input);

            //SolvePart2(test_input);
            SolvePart2(input);

        }
    }
}
