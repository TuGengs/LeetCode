# 二叉树的层次遍历 II

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :param root:    TreeNode
        :return:        List[List[int]]
        """
        results = []
        if not root:
            return results

        queue = [root]

        while queue:
            tmp = []
            # 由于queue会变化，所以不能用while
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:    # None
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))

            results.insert(0, tmp)

        return results

if __name__ == '__main__':
    a = Solution()

    x = TreeNode(3)
    x.left = TreeNode(9)
    x.right = TreeNode(20)
    x.right.left = TreeNode(15)
    x.right.right = TreeNode(7)

    l = a.levelOrderBottom(x)
    print(l)