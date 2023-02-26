class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        from collections import deque

        def path_to_root(parent_map, index):
            path_index = [index]
            while True:
                index = parent_map[index][1]
                if index == -1:
                    break
                path_index.append(index)
            return path_index

        def lowest_common_ancestor(root, a, b):
            q = deque()
            q.append((root, -1))
            parent_map = []
            p_index = q_index = None

            while len(q) > 0:
                node, parent = q.popleft()
                parent_map.append((node, parent))
                if node == a:
                    p_index = len(parent_map)-1
                if node == b:
                    q_index = len(parent_map)-1
                if node.left is not None:
                    q.append((node.left, len(parent_map)-1))
                if node.right is not None:
                    q.append((node.right, len(parent_map)-1))
            
            path_p = path_to_root(parent_map, p_index)
            path_p = set(path_p)
            path_q = path_to_root(parent_map, q_index)

            for index in path_q:
                if index in path_p:
                    return parent_map[index][0]

        return lowest_common_ancestor(root, p, q)
