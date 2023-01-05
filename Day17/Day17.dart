import 'dart:io';
import "dart:math";

String velocities = """23,-10 25,-9 27,-5 29,-6 22,-6 21,-7 9,0 27,-7 24,-5 25,-7 26,-6 25,-5 6,8 11,-2 20,-5 29,-10 6,3 28,-7 8,0 30,-6 29,-8 20,-10 6,7 6,4 6,1 14,-4 21,-6 26,-10 7,-1 7,7 8,-1 21,-9 6,2 20,-7 30,-10 14,-3 20,-8 13,-2 7,3 28,-8 29,-9 15,-3 22,-5 26,-8 25,-8 25,-6 15,-4 9,-2 15,-2 12,-2 28,-9 12,-3 24,-6 23,-7 25,-10 7,8 11,-3 26,-7 7,1 23,-9 6,0 22,-10 27,-6 8,1 22,-8 13,-4 7,6 28,-6 11,-4 12,-4 26,-9 7,4 24,-10 23,-8 30,-8 7,0 9,-1 10,-1 26,-5 22,-9 6,5 7,5 23,-6 28,-10 10,-2 11,-1 20,-9 14,-2 29,-7 13,-3 23,-5 24,-8 27,-9 30,-7 28,-5 21,-10 7,9 6,6 21,-5 27,-10 7,2 30,-9 21,-8 22,-7 24,-9 20,-6 6,9 29,-5 8,-2 27,-8 30,-5 24,-7""";


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
    return ( (this.x >= this.target_x_min && this.x <= this.target_x_max) && (this.y >= this.target_y_min &&  this.y <= this.target_y_max));
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

List<int> height_passed(int vec){
  List<int> height_passed = [];
  for (int i=0; i < 100; i++){
    height_passed.add(vec);
    vec--;
  }
  return height_passed;
}

void solve({ required int target_min_x, required int target_max_x, required int target_min_y, required int target_max_y}){

  // try various combinations

  // get the x_values that would work

  List<int> possible_x_values = List.generate(10000, (index) => index);
  possible_x_values = possible_x_values.where((number) => (factorial(number) >= target_min_x && factorial(number) <= target_max_x) ).toList();
  print(possible_x_values);

  List<int> possible_y_values = List.generate(1000, (index) => index-500);

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
  while (probe.x < max_x && probe.y >= min_y) {
    probe.step(draw:false);
    if (probe.on_target()){
      return true;
    }
  }
  return false;
}

void evaluate_velocities({ required int target_min_x, required int target_max_x, required int target_min_y, required int target_max_y}) {

  List<List<String>> velos = parse_velocities();
  List<List<int>> possible_velos = [];

  velos.forEach((element) {
    int x = int.parse(element[0]);
    int y = int.parse(element[1]);

    if (factorial(x) >= target_min_x && factorial(x) <=target_max_x){
      possible_velos.add([x,y]);
    }

    var final_list = [];

    possible_velos.forEach((velo) {
      int vx = velo[0];
      int vy = velo[1];
      int y = 0;
      while(y > target_min_y){
        if (y >= target_min_y && y <= target_max_y){
          final_list.add([x,y]);
          break;
        }
        y += vy;
        vy-=1;
      }


    });

    print(final_list);

  });

  print(possible_velos);


}

dynamic parse_velocities(){
    var v = velocities.split(" ");
    var numbers = v.map( (String element)=> element.split(',')).toList();

    return numbers;
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

    evaluate_velocities(target_min_x: 269,
      target_max_x: 292,
      target_min_y: -68,
      target_max_y: -44);

}
