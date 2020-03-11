# 整数反转
# way_1
# x % 10 = 个位数
# x // = 10
################################################################
# way_ 2 the following 按字符串反转来做
class Solution:
    def reverse(self, x):
        x = str(x)
        if x[0] == '-':
            y = "-" + x[:0:-1]
        else:
            y = x[::-1]
        y  = int(y)
        return y if -2147483648 < y < 2147483647 else 0

if __name__ == '__main__':
    a = Solution()
    l = a.reverse(1534469)
    print(l)