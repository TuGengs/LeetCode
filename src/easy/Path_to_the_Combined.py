# 路径总和

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        import collections
        deq = collections.deque([(root.val, root), ])
        while deq:
            d, node = deq.pop()
            if node.left:
                deq.append((d + node.left.val, node.left))
            if node.right:
                deq.append((d + node.right.val, node.right))
            if not node.left and not node.right:
                if sum == d:
                    return True
        return False

if __name__ == '__main__':
    a = Solution()
    l = a.hasPathSum(None)
    print(l)