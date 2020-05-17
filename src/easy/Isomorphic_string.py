# 同构字符串

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            m, n = s[i], t[i]
            if m in hash_s and hash_s[m] != n or (n in hash_t and hash_t[n] != m):
                return False
            hash_s[m] = n
            hash_t[n] = m

        return True

if __name__ == '__main__':
    a = Solution()
    l = a.isIsomorphic("ab", "aa")
    print(l)