# 二进制求和

class Solution:
    # 二进制 -> 十进制(计算) -> 二进制 最快！！！
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # 逐位运算
    def addBinary2(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)   # 填充保证长度一致

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:  # 1 3 5...
                answer.insert(0, '1')
            else:
                answer.insert(0, '0')

            carry //= 2

        if carry == 1:
            answer.insert(0, '1')

        return ''.join(answer)

    # 位运算
    def addBinary3(self, a: str, b: str) -> str:
        # 位运算也得在十进制层面操作
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y          # XOR 计算当前 xx 和 yy 的无进位相加结果
            carry = (x & y) << 1    # &   计算当前 xx 和 yy 的进位
            x, y = answer, carry    # 直到 carry = 0 才结束！
        return bin(x)[2:]

if __name__ == '__main__':
    a = Solution()
    l = a.addBinary2("11", "1")
    print(l)