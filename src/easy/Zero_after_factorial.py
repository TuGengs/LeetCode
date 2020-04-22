# 阶乘后的零 (有点意思)
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while n > 0:
            count += n // 5
            n //= 5

        return count