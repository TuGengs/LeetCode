# 多数元素

class Solution:
    # hash表计数法
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        import collections
        nums_cnt = collections.Counter(nums)

        for n in nums_cnt:
            if nums_cnt[n] > len(nums) // 2:
                return n


    # Boyer-Moore 投票算法
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == '__main__':
    a = Solution()
    l = a.majorityElement([2,2,1,1,1,2,2])
    print(l)
