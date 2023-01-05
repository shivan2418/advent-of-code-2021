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
      { required int this.x_velocity, required int this.y_velocity, required int this.target_x_min, required int this.target_x_max, required int this.target_y_min, required int this.target_y_max}) {
  }

  void step({bool draw = true}) {

    this.points.add(Point(x,y));

    this.x += this.x_velocity;
    this.y += this.y_velocity;

    if (this.x_velocity != 0) {
      int mod = this.x_velocity > 0 ? 1 : -1;
      this.x_velocity += mod;
    }
    this.y_velocity -= 1;

    if (draw) {
      int min_y = min(this.y, this.target_y_min);
      int max_y = max(this.y, this.target_y_max);
      int min_x = 0;
      int max_x = max(this.target_x_max, this.x);

      for (int y = max_y; y > min_y; y--) {
        for (int x = min_x; x <= max_x; x++) {
          if (x == 0 && y == 0) {
            stdout.write('S');
          }
          else if ( (x == this.x && y == this.y) || this.points.contains(Point(x,y))) {
            stdout.write("#");
          } else {

            if (x>=this.target_x_min && x<=this.target_x_max && y>=this.target_y_min && y<=this.target_y_max){
              stdout.write("X");
            } else {
              stdout.write(".");
            }
          }

        }
        print('');
      }
      print('');
    }
  }
}

void main() {
    var probe = new Probe(x_velocity: 2,
        y_velocity: 6,
        target_x_min: test_x_min,
        target_x_max: test_x_max,
        target_y_min: test_y_min,
        target_y_max: test_y_max);


    while (probe.x < test_x_max*2) {
      probe.step();
    }

  }
