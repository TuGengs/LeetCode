# 两数之和
# way_1
# num2 = target - num1
################################################################
# way_2 the following
# The dictionary records the values and locations of num1 and num2, eliminating the need to find the num2 index again.
################################################################
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for id, num in enumerate(nums):
            hashmap[num] = id
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]
if __name__ == '__main__':
    a = Solution()
    l = a.twoSum([1, 4, 9, 2, 10], 12)
    print(l)
