def depth(node):
    if Node is None:
        return -1

    left = depth(node.left)
    right = depth(node.right)

    return max(left, right) + 1
