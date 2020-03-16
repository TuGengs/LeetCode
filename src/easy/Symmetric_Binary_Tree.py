# 对称二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isMirror(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False

        return a.val == b.val and self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)

    # 递归
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def check(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return True
        if a.val != b.val:
            return False

    # 迭代
    def isSymmetric2(self, root: TreeNode) -> bool:
        import collections
        deq = collections.deque([(root, root), ])
        while deq:
            p, q = deq.popleft()

            if not self.check(p, q):
                return False

            # 遍历到的None节点（中间或最后），这里不可能为空树，也不可能是None和非None，不然上面直接return false
            if p or q:
                deq.append((p.left, q.right))
                deq.append((p.right, q.left))

        return True


if __name__ == '__main__':
    a = Solution()
    l = a.isSymmetric(None)
    print(l)