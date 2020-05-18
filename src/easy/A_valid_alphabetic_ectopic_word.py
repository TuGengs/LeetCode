# 有效的字母异位词

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        chars_cns = collections.Counter(s)
        chars_cnt = collections.Counter(t)

        return chars_cns == chars_cnt

if __name__ == '__main__':
    a = Solution()
    l = a.isAnagram("anagram", "nagaram")
    print(l)