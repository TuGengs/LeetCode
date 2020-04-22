# Excel表列序号

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        i = 0
        res = 0
        for tmp in s:
            res += (ord(tmp) - ord('A') + 1)  * (26 ** i)
            i += 1

        return res

if __name__ == '__main__':
    a = Solution()
    l = a.titleToNumber("ZY")
    print(l)