# 二叉树的最小深度

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        result = 2 << 30
        import collections
        deq = collections.deque([(depth, root), ])
        while deq:
            depth, node = deq.popleft()
            if node:  # None
                deq.append((depth + 1, node.left))
                deq.append((depth + 1, node.right))
                if not node.left and not node.right:
                    result = depth + 1 if depth < result else result
            # 剪枝
            if depth + 1 > result:
                break
        return result

    # DFS
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 2 << 30
        import collections
        deq = collections.deque([(0, root), ])
        while deq:
            d, node = deq.pop()
            if node:
                deq.append((d + 1, node.left))
                deq.append((d + 1, node.right))
                if not node.left and not node.right:
                    result = d + 1 if d < result else result
        return result

if __name__ == '__main__':
    a = Solution()
    l = a.minDepth(None)
    print(l)