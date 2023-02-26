import functools

def smallest_from_leaf(root):

    parents = []
    leaf_nodes = []
    queue = deque()
    queue.append((root, -1))

    while len(queue) > 0:
        node, parent = queue.popleft()
        parents.append((node, parent))
        if node.left is None and node.right is None:
            leaf_nodes.append(len(parents)-1)
            continue
        if node.left is not None:
            queue.append((node.left, len(parents)-1))
        if node.right is not None:
            queue.append((node.right, len(parents)-1))
        
    words = []
    for idx in leaf_nodes:
        word = []
        while True:
            node, parent = parents[idx]
            word.append(chr(ord('a') + node.val))
            if parent == -1:
                break
            idx = parent
        word = ''.join(word)
        words.append(word)
    
    words.sort()
    return words[0]
