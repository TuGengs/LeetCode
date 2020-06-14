# 转变数组后最接近目标值的数组和   利用单调性(可用二分查找法进行优化)

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        pre = 0

        print(arr)
        for i, a in enumerate(arr):
            k = len(arr) - i        # k > 0
            d = pre + a * k - target    #sum = pre + a * k .
            if d >= 0:
                res = a - (d * 1.0) / k
                if res - int(res) <= 0.5:
                    return int(res)
                else:
                    return int(round(res))
            pre += a

        return arr[-1]

if __name__ == '__main__':
    a = Solution()
    l = a.findBestValue([4,9,3], 10)
    print(l)