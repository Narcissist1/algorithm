from .utils import Node
from collections import deque

visited = set()
queue = deque()

def bfs(nroot):
    queue.appendleft(nroot)
    while queue:
        current_node = queue.pop()
        print(current_node.mesg)
        visited.add(current_node._id)
        if current_node.nodes:
            for node in current_node.nodes:
                if node._id not in visited:
                    queue.appendleft(node)


if __name__ == '__main__':
    root = Node(0)
    root.add_childs([Node(1), Node(2), Node(3)])
    root.nodes[0].add_childs([Node(4), Node(5)])
    root.nodes[1].add_childs([Node(6), Node(7)])
    root.nodes[2].add_childs([Node(8), Node(9)])
    bfs(root)