def distribute_coins(self, node):
        if node is None:
            return 0
        left  = self.distribute_coins(node.left)
        right = self.distribute_coins(node.right)
        self.moves += (abs(left) + abs(right))
        return node.val + left + right - 1