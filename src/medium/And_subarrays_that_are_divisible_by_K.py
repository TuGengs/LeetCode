# 和可被 K 整除的子数组

class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        map = {0 : 1}
        presum = 0
        count = 0

        for i in range(len(A)):
            presum = (presum + A[i]) % K
            if presum < 0:
                presum += K
            if presum in map:
                count += map[presum]
                map[presum] += 1
            else:
                map[presum] = 1
        return count

if __name__ == '__main__':
    a = Solution()
    l = a.subarraysDivByK([4,5,0,-2,-3,1], 5)
    print(l)