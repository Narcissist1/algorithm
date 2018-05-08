var _id = 0
function node(name, nodes) {
    this.name = name;
    this.nodes = nodes === undefined ? [] : nodes;
    this._id = _id;
    _id++;
    this.addChildren = function (nodes) {
        this.nodes = this.nodes.concat(nodes);
    }
}

module.exports = {
    node: node
}