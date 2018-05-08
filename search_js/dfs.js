var node = require('./utils').node;
var stack = [];
var visited = new Set();


function bfs(nroot) {
    stack.push(nroot);
    while (stack.length != 0) {
        current_node = stack.pop();
        console.log(current_node.name);
        visited.add(current_node);
        if (current_node.nodes.length != 0) {
            for (node of current_node.nodes) {
                if (!visited.has(node._id)) {
                    stack.push(node);
                }
            }
        }
    }
}

(function main() {
    rootNode = new node(0);
    rootNode.addChildren([new node(1), new node(2), new node(3)]);
    rootNode.nodes[0].addChildren([new node(4), new node(5)]);
    rootNode.nodes[1].addChildren([new node(6), new node(7)]);
    rootNode.nodes[2].addChildren([new node(8), new node(9)]);
    bfs(rootNode);
})();