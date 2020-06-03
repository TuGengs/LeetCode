# 新21点 (爱丽丝获胜的概率只和下一轮开始前的得分有关，因此根据得分计算概率。)

class Solution:
    def new21Game(self, N, K, W):   # < K 抽，< N 赢
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """

        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W

        # dp 动态规划
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]

if __name__ == '__main__':
    a = Solution()
    l = a.new21Game(6, 1, 10)
    print(l)