# strStr

class Solution:
    # 直接内置find，另外，双指针法也OK，时间复杂度和Rabin Karp一样，O(N)
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # Rabin Karp https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/
    # 属于单指针情况下的拓展，一次性计算needle长度的str的hash值来进行比较。
    def strStr2(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        a = 26
        modulus = 2 ** 31
        h_to_int = lambda i: ord(haystack[i]) - ord('a')
        needle_to_int = lambda i: ord(needle[i]) - ord('a')

        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0

        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1

if __name__ == '__main__':
    a = Solution()
    l = a.strStr("asddsadasd", "sa")
    print(l)