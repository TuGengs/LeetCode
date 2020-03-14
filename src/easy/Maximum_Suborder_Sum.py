# 最大子序和

class Solution:
    # 贪心法   O(n)
    # 子序列一定是正数开头，然后贪心寻找最优解，最后得到全局解。
    def maxSubArray(self, nums):

        """
        :param nums:    List[int]
        :return:        int
        """

        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

    # 动态规划法 Kadane  O(n)
    # 相比贪心法，少了一个nums[i - 1]等价于curr_sum。直接修改了sum数组作为dp[]，没太大区别。
    def maxSubArray2(self, nums):

        """
        :param nums:    List[int]
        :return:        int
        """

        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)

        return max_sum

    # 分治法   时间复杂度 O(nlogn)
    def maxSubArray3(self, nums):

        """
        :param nums:    List[int]
        :return:        int
        """

        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 采用贪心法，计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        # 从右往左 -> 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        # 从右往左 -> len - 1
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

if __name__ == '__main__':
    a = Solution()
    l = a.maxSubArray2([-2,1,-3,1,0,1,1,-1,2])
    print(l)