import 'package:tuple/tuple.dart';
import 'dart:math';
import "dart:io";

String test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""";

typedef Path = List<Location>;

Path parse_input(String input) {
  List<Location> locations = [];
  List<List<int>> risk_points = [];

  var rows = input.split("\n");
  rows.forEach((row) {
    var col = row.split('').map(int.parse).toList();
    risk_points.add(col);
  });

  int grid_height = rows.length;
  int grid_width = rows[0].length;

  for (int x = 0; x < grid_width; x++) {
    for (int y = 0; y < grid_height; y++) {
      var new_location = Location(x, y, risk_points[x][y],
          start: x == 0 && y == 0,
          end: x == grid_width - 1 && y == grid_height - 1);
      locations.add(new_location);
    }
  }
  return locations;
}

class Location {
  int x;
  int y;
  int risk;
  bool start = false;
  bool end = false;

  dynamic distance_from_origin = double.infinity;
  dynamic previous_vertex = null;

  late Location? top;
  late Location? bottom;
  late Location? left;
  late Location? right;

  Location(this.x, this.y, this.risk, {this.start = false, this.end = false});

  Path get_neighbours(){
    List<Location> neighbours = [];
    if (top != null) neighbours.add(top!);
    if (bottom != null) neighbours.add(bottom!);
    if (left != null) neighbours.add(left!);
    if (right != null) neighbours.add(right!);
    return neighbours;
  }

}

class RiskGrid {
  late int width;
  late int height;
  late Map<Tuple2<int, int>, Location> grid;
  late Location origin;


  RiskGrid(String input) {
    List<Location> locations = parse_input(input);
    width = locations.map((e) => e.x).reduce(max) + 1;
    height = locations.map((e) => e.y).reduce(max) + 1;

    Map<Tuple2<int, int>, Location> grid_map = {};

    locations.forEach((Location loc) {
      grid_map[Tuple2(loc.x, loc.y)] = loc;
    });
    grid = grid_map;
    origin = grid[Tuple2(0, 0)]!;
    origin.distance_from_origin = 0;
    set_location_neighbours();
  }

  void set_location_neighbours() {
    grid.forEach((key, value) {
      value.top = grid[Tuple2(value.x, value.y - 1)];
      value.bottom = grid[Tuple2(value.x, value.y + 1)];
      value.left = grid[Tuple2(value.x - 1, value.y)];
      value.right = grid[Tuple2(value.x + 1, value.y)];
    });
  }

  static get_path_risk(List<Location> path) {
    path = path.where((element) => element.start == false).toList();
    return path.map((e) => e.risk).reduce((value, element) => value + element);
  }

  Location? get_loc(int x, int y) {
    return this.grid[Tuple2(x, y)];
  }

  Path get_base_path() {
    // calculate the native path from the origin to the target
    Path path = [origin];
    Location current = origin;
    while (current.end == false) {
      if (current.bottom != null) {
        path.add(current.bottom!);
        current = current.bottom!;
      } else {
        path.add(current.right!);
        current = current.right!;
      }
    }
    return path;
  }

  void print_path(Path path) {
    for (int y = 0; y < this.height; y++) {
      for (int x = 0; x < this.width; x++) {
        Location? loc = get_loc(x, y);
        if (path.contains(loc)) {
          stdout.write('*');
        } else {
          stdout.write(this.get_loc(x, y)?.risk);
        }
      }
      print('');
    }
  }
}

void diks_algo(RiskGrid grid) {


  Map distance_map = {};

  var unvisited = grid.grid.values.toList();

  List<Location> visited = [];

  // start at origin
  Location current = grid.origin;

  var adjacent = current.get_neighbours();
  adjacent.forEach((element) {
    int distance = element.risk;
    if (distance < element.distance_from_origin) {
      element.distance_from_origin = distance;
      element.previous_vertex = current;
    }
  });






}


void main() {
  RiskGrid grid = RiskGrid(test_input);

  diks_algo(grid);


}
