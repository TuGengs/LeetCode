# 罗马数字转整数
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# way_1
# 遍历整个 s 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，
# 如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
# d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
#             'CM': 800, 'M': 1000}
# sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))
################################################################
# way_2 the following
# 全部相加，如果有小数在大数后面就减双倍的小数字
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            sum += d[s[i]]
            if i > 0 and d[s[i]] > d[s[i - 1]]:
                sum -= 2 * d[s[i - 1]]
        return sum

if __name__ == '__main__':
    a = Solution()
    l = a.romanToInt('IV')
    print(l)