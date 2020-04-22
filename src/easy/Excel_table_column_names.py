# Excel表列名称

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        res = ''
        while n > 26:
            count = n % 26
            if count == 0:
                res += chr(ord('A') + 25)
                n = n // 26 - 1
            else:
                res += chr(ord('A') + count - 1)
                n = n // 26

        res += chr(ord('A') + n - 1)

        res = res[::-1]
        return res

if __name__ == '__main__':
    a = Solution()
    l = a.convertToTitle(701)
    print(l)