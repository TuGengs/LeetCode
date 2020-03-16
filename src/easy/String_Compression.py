# 字符串压缩

class Solution:
    def compressString(self, S: str) -> str:

        if not S:
            return S

        p1 = 0
        tmp = ""

        for p2 in range(len(S)):
            if S[p2] != S[p1]:
                tmp += S[p1]
                tmp += str(p2 - p1)
                p1 = p2

        tmp += S[p1]
        tmp += str(p2 - p1 + 1)

        return tmp if len(tmp) < len(S) else S

if __name__ == '__main__':
    a = Solution()
    l = a.compressString("aabcccccaaa")
    print(l)