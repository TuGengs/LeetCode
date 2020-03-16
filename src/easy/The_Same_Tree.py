# 相同的树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    out_list_temp = []
    out_list_temp2 = []
    out_list_temp3 = []

    def preorder_traversal(self, tree):
        if (tree.val != None):
            self.out_list_temp.append(tree.val)
        if tree.left != None:
            self.preorder_traversal(tree.left)
        if tree.right != None:
            self.preorder_traversal(tree.right)

    def inorder_traversal(self, tree):
        if tree.left != None:
            self.inorder_traversal(tree.left)
        if (tree.val != None):
            self.out_list_temp2.append(tree.val)
        if tree.right != None:
            self.inorder_traversal(tree.right)

    def postorder_traversal(self, tree):

        if tree.left != None:
            self.postorder_traversal(tree.left)
        if tree.right != None:
            self.postorder_traversal(tree.right)
        if (tree.val != None):
            self.out_list_temp3.append(tree.val)

    # 前序 + 中序 ／ 后序 + 中序 可以唯一标识一颗二叉树 (X) 比如[1, 1]和[1, null, 1]就不行（元素均不相同则可以， 或者利用访问的节点的索引而不是值）
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        self.out_list_temp = []
        self.out_list_temp2 = []

        self.preorder_traversal(p)
        self.inorder_traversal(p)
        p_tra = self.out_list_temp + self.out_list_temp2

        self.out_list_temp = []
        self.out_list_temp2 = []

        self.preorder_traversal(q)
        self.inorder_traversal(q)
        q_tra = self.out_list_temp + self.out_list_temp2

        self.out_list_temp = []
        self.out_list_temp2 = []

        return p_tra == q_tra

    # 递归
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

    def check(self, p, q):
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return True

    # 迭代    不像递归，每次会自动重复check，所以，这里封装一个check函数。
    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:

        self.check(p, q)

        import collections
        deq = collections.deque([(p, q), ])

        while deq:
            p, q = deq.popleft()

            if not self.check(p, q):
                return False

            # 遍历到的None节点（中间或最后），这里不可能为空树，也不可能是None和非None，不然上面直接return false
            if p or q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

if __name__ == '__main__':
    a = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)
    l = a.isSameTree3(t1, t2)
    print(l)