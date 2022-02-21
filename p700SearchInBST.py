def BSTSearch(node, key):

    while True:
        if node is None or key == node.val:
            return node
        node = node.left if key < node.val else node.right
        