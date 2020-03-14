# 外观数列

class Solution:

    # 递归
    def Say(self, n: str) -> str:
        rtn = ""
        pi = 0
        pj = 0
        while pi < len(n):
            while pj < len(n):
                if n[pi] == n[pj]:
                    pj += 1
                    if pj >= len(n):
                        rtn += str(pj - pi) + str(n[pi])
                        break
                else:
                    rtn += str(pj - pi) + str(n[pi])
                    break
            pi = pj

        return rtn

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.Say(self.countAndSay(n - 1))

    # 迭代
    def countAndSay2(self, n: int) -> str:
        rs = "1"
        for i in range(2, n + 1):
            rs = self.Say(rs)
        return rs

if __name__ == '__main__':
    a = Solution()
    l = a.countAndSay2(5)
    print(l)