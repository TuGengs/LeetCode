# x 的平方根

from math import e, log

class Solution:
    # 内置
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)

    # 袖珍计算器算法   O(1)
    def mySqrt2(self, x: int) -> int:
        if x < 2:
            return int(x)
        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

    # 牛顿法  O(log(n))   https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode/
    def mySqrt3(self, x: int) -> int:
        if x < 2:
            return x
        x0 = x
        x1 = (x0 + x / x0) / 2

        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)

if __name__ == '__main__':
    a = Solution()
    l = a.mySqrt3(4)
    print(l)