# 爬楼梯

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 4:
            return n

        dp_1 = 3
        dp_2 = 2

        for i in range(4, n + 1):
            tmp = dp_1 + dp_2
            if i == n:
                return tmp
            dp_2 = dp_1
            dp_1 = tmp

if __name__ == '__main__':
    a = Solution()
    l = a.climbStairs(100)
    print(l)