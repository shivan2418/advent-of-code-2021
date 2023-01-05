import 'dart:io';
import "dart:math";

int test_x_min = 20;
int test_x_max = 30;
int test_y_min = -10;
int test_y_max = -5;

class Probe {
  List<Point> points = [];

  int x = 0;
  int y = 0;
  int x_velocity;
  int y_velocity;

  int target_x_min;
  int target_x_max;
  int target_y_min;
  int target_y_max;

  Probe(
      {required int this.x_velocity,
      required int this.y_velocity,
      required int this.target_x_min,
      required int this.target_x_max,
      required int this.target_y_min,
      required int this.target_y_max}) {}

  int get_max_x() {
    return this.points.map((point) => point.x).reduce(max).toInt();
  }

  int get_max_y() {
    return this.points.map((point) => point.y).reduce(max).toInt();
  }

  String get_char(int x, int y) {
    if (x == 0 && y == 0) return "S";

    if (x >= this.target_x_min &&
        x <= this.target_x_max &&
        y >= this.target_y_min &&
        y <= this.target_y_max) {
      if (this.points.contains(Point(x, y))) {
        return "O";
      } else{
        return "T";
      }
    }

    if (this.points.contains(Point(x, y))) {
      return "#";
    }

    return ".";
  }

  void draw() {
    int min_y = min(this.y, this.target_y_min);
    int max_y = [this.get_max_y(), this.y, this.target_y_max].reduce(max);
    int min_x = 0;
    int max_x = max(this.target_x_max, this.x);

    for (int y = max_y; y > min_y; y--) {
      for (int x = min_x; x <= max_x; x++) {
       stdout.write(get_char(x, y));
      }
      print("");
    }
    print('vel-x $x_velocity vel-y:$y_velocity');
  }

  bool on_target(){
    return (this.x >= this.target_x_min &&
        this.x <= this.target_x_max &&
        this.y >= this.target_y_min &&
        this.y <= this.target_y_max);
  }

  void step({bool draw = true}) {
    this.points.add(Point(x, y));

    this.x += this.x_velocity;
    this.y += this.y_velocity;

    if (this.x_velocity > 0) {
      this.x_velocity--;
    } else if (this.x_velocity < 0) {
      this.x_velocity++;
    }
    this.y_velocity -= 1;

    if (draw) {
      this.draw();
    }
  }
}


int factorial(int vec){
  int sum = 0;
  while (vec>0){
    sum+=vec;
    vec--;
  }
  return sum;
}

void solve({ required int target_min_x, required int target_max_x, required int target_min_y, required int target_max_y}){

  // try various combinations

  // get the x_values that would work

  List<int> possible_x_values = List.generate(10000, (index) => index);
  possible_x_values = possible_x_values.where((number) => (factorial(number) >= target_min_x && factorial(number) <= target_max_x) ).toList();
  print(possible_x_values);

  List<int> possible_y_values = List.generate(1000, (index) => index+3);

  List<Probe> probes = [];

  possible_x_values.forEach(( int x) {
    possible_y_values.forEach((int y) {
      Probe new_probe = new Probe(target_x_max: target_max_x,target_x_min: target_min_x,target_y_max: target_max_y,target_y_min: target_min_y,x_velocity: x,y_velocity: y);
      probes.add(new_probe);
    });
  });

  List<Probe> successful_probes = probes.where( (Probe probe) => test_launch(probe,target_max_x,target_min_y)
  ).toList();

  Probe highest_probe = successful_probes.first;

  successful_probes.forEach((probe) {
    if (probe.get_max_y() > highest_probe.get_max_y()){
      highest_probe = probe;
    }
  });
  print('highest Y: ${highest_probe.get_max_y()}');

}

bool test_launch(Probe probe, int max_x, int min_y){
  while (probe.x < max_x && probe.y > min_y) {
    probe.step(draw:false);
    if (probe.on_target()){
      return true;
    }
  }
  return false;
}

void main() {
  solve(target_min_x: test_x_min,
      target_max_x: test_x_max,
      target_min_y: test_y_min,
      target_max_y: test_y_max);

  solve(target_min_x: 269,
      target_max_x: 292,
      target_min_y: -68,
      target_max_y: -44);
}
