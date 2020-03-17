# 将有序数组转换为二叉搜索树 (答案不唯一 P选择中间偏左和偏右两种方法都可以)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def helper(self, left, right, nums):
        if left > right:
            return None

        p = (left + right) // 2

        # 1. 先写递归关系，再return
        # 2. 写if return 再return 递归关系
        # 3. return 递归关系 + - * ／ 常数
        root = TreeNode(nums[p])
        root.left = self.helper(left, p - 1, nums)
        root.right = self.helper(p + 1, right, nums)

        return root

    def sortedArrayToBST(self, nums):
        """
        :param nums:    List[int]
        :return:        TreeNode
        """
        return self.helper(0, len(nums) - 1, nums)

if __name__ == '__main__':
    a = Solution()
    l = a.sortedArrayToBST([-10,-3,0,5,9])
    print(l)