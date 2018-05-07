
class Node:
    def __init__(self, mesg, left_node=None, right_node=None):
        self.mesg = mesg

    def add_childs(self, nodes):
        self.nodes = nodes

def dfs(nroot):
    stack = []
    stack.append(nroot)
    while stack:
        current_node = stack.pop()
        print(current_node.mesg)
        if current_node.left_node:
            stack.append(current_node.left_node)
        if current_node.right_node:
            stack.append(current_node.right_node)

if __name__ == '__main__':
    root = Node('root')