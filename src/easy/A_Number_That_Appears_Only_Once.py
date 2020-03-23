# 只出现一次的数字

class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    # 2 * (a + b + c) − (a + a + b + b + c) = c
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    # XOR
    # a ⊕ 0 = a
    # a ⊕ a = 0
    # a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b
    def singleNumber3(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == '__main__':
    a = Solution()
    l = a.singleNumber3([1,1,2,2,3])
    print(l)