# 打家劫舍

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        pre = 0
        ppre = 0

        for n in nums:
            current = max(ppre + n, pre)
            ppre = pre
            pre = current

        return current


if __name__ == '__main__':
    a = Solution()
    l = a.rob([2,7,9,3,1])
    print(l)