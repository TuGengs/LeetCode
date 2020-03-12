# 回文数

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

if __name__ == '__main__':
    a = Solution()
    l = a.isPalindrome(-121)
    print(l)