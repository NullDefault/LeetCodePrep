"""
~Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # Base case
        if root is None:
            return []

        # Enqueue root and initialize height
        q = [root]
        ship_back = []
        level = 0
        while q:
            # nodeCount (queue size) indicates number
            # of nodes at current level.
            count = len(q)

            # Dequeue all nodes of current level and
            # Enqueue all nodes of next level
            while count > 0:
                node = q.pop(0)

                try:
                    ship_back[level].append(node.val)
                except:
                    ship_back.append([node.val])

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                count -= 1
            level = level + 1

        return ship_back


class CleanSolution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            result.append([])
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                result[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
