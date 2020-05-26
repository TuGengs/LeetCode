# 寻找重复数

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # node = index of nums
        # node.next = nums[node]
        # node.next.next = nums[nums[node]]
        slow = nums[0]  # 先走一步
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]  # 曾经犯的一个错误，以为这里会固定地在环入口，值相同的那个点相遇

        root = 0                     # 其实它们可以在环上任何一个node相遇，这里就是任何一个数组的下标index

        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow     # 回到循环结束的上一步
                        # nums[proot] == nums[pslow]
                        # The last slow = nums[proot] and this value at least has two slot in the array

if __name__ == '__main__':
    a = Solution()
    l = a.findDuplicate(None)
    print(l)
