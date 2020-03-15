# 爬楼梯

class Solution:
    # 这与斐波那契数列一致，所以，转换成为n阶斐波那契数列。
    # climb[n] = climb[n - 1] + climb[n - 2]
    def climbStairs(self, n: int) -> int:
        sqrt_5 = 5 ** 0.5
        return int(((((1 + sqrt_5) / 2) ** (n + 1)) - (((1 - sqrt_5) / 2) ** (n + 1))) / sqrt_5)

    # 动态规划 || 递归法 dp数组换成递归的形式即可。（可加入记忆化数组，优化 递归方法|| 动态规划）
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
    a = Solution()
    l = a.climbStairs2(3)
    print(l)