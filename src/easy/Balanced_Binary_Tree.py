# 平衡二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def height(self, root: TreeNode) -> int:
        if not root:
            return -1   # 抵消 1 + []
        return 1 + max(self.height(root.left), self.height(root.right))

    # 自顶向下的递归   O(nlogn)
    # 每一个节点都计算他的深度，然后做判断abs
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, -1

        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0

        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    # 自底向上的递归   O(n)
    # 自顶向下可以采用 1 + 的形式递归求得，但是自底向上只能用变量height暂存，因为Height不是递增的。
    def isBalanced2(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


if __name__ == '__main__':
    a = Solution()
    l = a.isBalanced(None)
    print(l)