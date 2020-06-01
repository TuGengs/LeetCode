# 拥有最多糖果的孩子

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        tmp = max(candies)
        return [True if i + extraCandies > tmp else False for i in candies]

if __name__ == '__main__':
    a = Solution()
    l = a.kidsWithCandies(None, None)
    print(l)