
export default class Node {
    up?: Node;
    down?: Node;
    left?: Node;
    right?: Node;

    start:boolean = false;
    end:boolean = false;

    visited:boolean = false;

    distance_from_start:number = Infinity;
    previous_node?:Node;

    toString():string {
        return `(${this.x},${this.y})`;
    }

    constructor(public x:number, public y:number, public cost:number) {
    }

    get_distance_to_previous(previous:Node){

        let cost = previous.cost + this.cost;
        return cost;
    }

    get_distance_from_start(arrived_via?:Node):number {

        let cost = this.cost;
        let previous = this.previous_node || arrived_via as Node;

        while (!previous!.start) {
            cost += previous!.cost;
            previous = previous!.previous_node!;
        }
        return cost;
    }

    get_neighbors():Node[] {
        let neighbors:Node[] = [];
        if (this.up) neighbors.push(this.up);
        if (this.down) neighbors.push(this.down);
        if (this.left) neighbors.push(this.left);
        if (this.right) neighbors.push(this.right);
        return neighbors;
    }

    get_unvisited_neighbors():Node[] {
        let neighbors = this.get_neighbors();
        return neighbors.filter( (neighbor) => !neighbor.visited );
    }

    static get_next_node_to_visit(nodes:Node[]):Node|undefined {

        nodes = nodes.filter( (node) => !node.visited );
        nodes = nodes.sort( (a,b) => a.distance_from_start - b.distance_from_start );
        return nodes[0];
    }

    _make_key(mod_x=0,mod_y=0):string {
        return `${this.x+mod_x}-${this.y+mod_y}`;
    }

    get_up(node_map:Map<string,Node>):Node|undefined {
        return node_map.get(this._make_key(0,-1));
    }

    get_down(node_map:Map<string,Node>):Node|undefined {
        return node_map.get(this._make_key(0,1))

    }

    get_left(node_map:Map<string,Node>):Node|undefined {
        return node_map.get(this._make_key(-1,0));
    }

    get_right(node_map:Map<string,Node>):Node|undefined {
        return node_map.get(this._make_key(1,0));
    }
}
