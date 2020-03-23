# 买卖股票的最佳时机 暴搜会超出时间！

class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inf = int(1e9)
        min_price = inf
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)                   # 一直记录局部最小价格
            max_profit = max(price - min_price, max_profit)     # 一直记录局部最优利润

        return max_profit

if __name__ == '__main__':
    a = Solution()
    l = a.maxProfit([7,1,5,3,6,4])
    print(l)