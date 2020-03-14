# 加一

class Solution:

    # 从右往左走，模拟加法法则。
    def plusOne(self, digits):

        """
        :param digits:  List[int]
        :return:        List[int]
        """

        digits[len(digits) - 1] += 1
        if digits[len(digits) - 1] < 10:
            return digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                digits[i] = digits[i] % 10
                if i == 0:
                    digits.insert(0, 1)
                    break
                else:
                    digits[i - 1] += 1
        return digits

    # 从右往左走，遇大于9变0。
    def plusOne2(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits

    # str list int之间的转化
    # list[int] -> str -> int -> List[int]
    def plusOne3(self, digits):
        return [int(x) for x in str(int(''.join(str(s) for s in digits)) + 1)]

    # str list int之间的转化
    # list[int] -> int -> str -> List[int]
    def plusOne4(self, digits):
        num = digits[len(digits) - 1]
        j = 1
        for i in range(len(digits) - 2, -1, -1):
            num += digits[i] * (10 ** j)
            j += 1
        num += 1
        return [int(x) for x in str(num)]

if __name__ == '__main__':
    a = Solution()

    l = a.plusOne4([9,9,9])
    print(l)