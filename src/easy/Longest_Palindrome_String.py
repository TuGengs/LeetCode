# 最长回文串

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars_cnt = collections.Counter(s)
        tmp = 0
        nums = 0
        for i in chars_cnt:
            if tmp == 0 and chars_cnt[i] % 2 == 1:
                tmp = 1
            nums += chars_cnt[i] // 2

        return 2 * nums + tmp

    # 长度小于s，则一定有奇数个char存在。
    # 因为，nums += 2，然后还比你小，说明没有都用上。你品，你细品！
    def longestPalindrome2(self, s: str) -> int:
        chars_cnt = collections.Counter(s)
        nums = 0
        for i in chars_cnt:
            nums += 2 * (chars_cnt[i] // 2)

        return nums + (nums != len(s))

if __name__ == '__main__':
    a = Solution()
    l = a.longestPalindrome2("abccccdd")
    print(l)