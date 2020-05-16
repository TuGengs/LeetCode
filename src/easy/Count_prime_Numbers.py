# 计数质数

class Solution:

    # 厄拉多塞筛法，另外：判断是否为质数-孪生质数法！
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i : n : i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)

if __name__ == '__main__':
    a = Solution()
    l = a.countPrimes(100)
    print(l)