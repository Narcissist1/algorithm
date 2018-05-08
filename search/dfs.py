
visited = set()

class Node:
    _id = 0
    def __init__(self, mesg, nodes=None):
        self.mesg = mesg
        self.nodes = [] if nodes is None else nodes
        self._id = Node._id
        Node._id += 1

    def add_childs(self, nodes):
        self.nodes.extend(nodes)

def dfs(nroot):
    stack = []
    stack.append(nroot)
    while stack:
        current_node = stack.pop()
        print(current_node.mesg)
        visited.add(current_node._id)
        if current_node.nodes:
            for node in current_node.nodes:
                if not node._id in visited:
                    stack.append(node)


if __name__ == '__main__':
    root = Node(0)
    root.add_childs([Node(1), Node(2), Node(3)])
    root.nodes[0].add_childs([Node(4), Node(5)])
    root.nodes[1].add_childs([Node(6), Node(7)])
    root.nodes[2].add_childs([Node(8), Node(9)])
    dfs(root)
