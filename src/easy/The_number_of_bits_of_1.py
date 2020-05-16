# 位1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

if __name__ == '__main__':
    a = Solution()
    l = a.hammingWeight(43261596)
    print(l)