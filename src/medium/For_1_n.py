# 求1+2+…+n
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

class Solution:
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n != 0 and n + self.sumNums(n - 1)

    # 幂运算  (1 + n) * n / 2 = (n + n^2) / 2
    def sumNums2(self, n):
        return (n + n ** 2) >> 1

    # 快速乘法 https://leetcode-cn.com/problems/qiu-12n-lcof/solution/qiu-12n-by-leetcode-solution/

if __name__ == '__main__':
    a = Solution()
    l = a.sumNums(10)
    print(l)