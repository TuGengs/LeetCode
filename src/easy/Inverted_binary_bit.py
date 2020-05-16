# 颠倒二进制位

class Solution:
    def reverseBits(self, n: int) -> int:
        strn = bin(n)[2:]
        strn =  ''.join(reversed('0' * (32 - len(strn)) + strn))
        return int(strn, 2)

if __name__ == '__main__':
    a = Solution()
    l = a.reverseBits(43261596)
    print(l)