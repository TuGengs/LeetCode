# 二叉树的最大深度

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        import collections
        deq = collections.deque([(depth, root), ])
        while deq:
            depth, node = deq.popleft()
            if node:    # None
                deq.append((depth + 1, node.left))
                deq.append((depth + 1, node.right))

        return depth

    # DFS   注意是从右边出来！pop()
    def maxDepth2(self, root: TreeNode) -> int:
        depth = 0
        import collections
        deq = collections.deque([(depth, root), ])
        while deq:
            d, node = deq.pop()
            depth = max(depth, d)
            if node:
                deq.append((d + 1, node.left))
                deq.append((d + 1, node.right))
        return depth

    # DFS
    def maxDepth3(self, root: TreeNode) -> int:
        return max(self.maxDepth3(root.left), self.maxDepth3(root.right)) + 1 if root else 0

if __name__ == '__main__':
    a = Solution()

    x = TreeNode(3)
    x.left = TreeNode(9)
    x.right = TreeNode(20)
    x.right.left = TreeNode(15)
    x.right.right = TreeNode(7)

    l = a.maxDepth2(x)
    print(l)