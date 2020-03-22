# 验证回文串

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        pi = 0
        pj = len(s) - 1
        if pj == 0:
            return True
        while pi < pj:
            while not s[pi].isalpha() and not s[pi].isalnum():
                pi += 1
                if pi > len(s) - 1:
                    return True
            while not s[pj].isalpha() and not s[pj].isalnum():
                pj -= 1
                if pj < 0:
                    return True
            if s[pi].lower() == s[pj].lower():
                pi += 1
                pj -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    l = a.isPalindrome("A man, a plan, a canal: Panama")
    print(l)