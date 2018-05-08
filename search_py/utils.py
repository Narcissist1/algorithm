class Node:
    _id = 0
    def __init__(self, mesg, nodes=None):
        self.mesg = mesg
        self.nodes = [] if nodes is None else nodes
        self._id = Node._id
        Node._id += 1

    def add_childs(self, nodes):
        self.nodes.extend(nodes)
