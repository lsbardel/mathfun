def traverse(node, callback):
    """Traverse a binary tree without recursion
    """
    current = node
    processed = 0
    stack = []

    while current:
        if not processed:
            try:
                callback(current, stack)
            except StopIteration:
                break
            if current.left:
                stack.append((current, 1))
                current = current.left
                processed = 0
                continue

        if processed < 2:
            if current.right:
                stack.append((current, 2))
                current = current.right
                processed = 0
                continue

        # end of the tree
        try:
            current, processed = stack.pop()
        except IndexError:
            break


def preOrder(root):
    nodes = []
    traverse(root, lambda n, s: nodes.append(n))
    return " ".join((str(n.data) for n in nodes))


class CheckOrder:
    def __init__(self):
        self.max = None
        self.min = None
        self.result = True

    def __call__(self, node, stack):
        if not stack:
            self.max = node.data
            self.min = node.data
        else:
            prev = stack[-1]
            # left branch
            if prev.left is node:
                self.max = min(self.max, node.data)
                if node.data > self.max:
                    self.result = False
                    raise StopIteration
            # right branch
            elif prev.right is node:
                self.min
                if self.prev.data > node.data:
                    self.result = False
                    raise StopIteration


def check_binary_search_tree_(root):
    return "No" if traverse(root) is None else "Yes"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    node = Node(3)
    node.right = Node(2)
    node.right.left = Node(6)
    node.left = Node(5)
    node.left.left = Node(1)
    node.left.right = Node(4)
    print(preOrder(node))
