# 存在重复元素 II

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        res = {}
        for n in range(len(nums)):
            if nums[n] not in res:
                res[nums[n]] = n
            else:
                if abs(n - res[nums[n]]) <= k:
                    return True
                else:
                    res[nums[n]] = n
        return False

if __name__ == '__main__':
    a = Solution()
    l = a.containsNearbyDuplicate([1,2,3,1], 3)
    print(l)