# 买卖股票的最佳时机II 暴搜会超出时间！

class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res

if __name__ == '__main__':
    a = Solution()
    l = a.maxProfit([7,1,5,3,6,4])
    print(l)