# 快乐数

class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        p1 = n
        p2 = get_next(n)

        while p1 != p2 and p1 != 1 and p2 != 1:
            p1 = get_next(p1)
            p2 = get_next(get_next(p2))

        return p1 != p2 or p1 == 1 or p2 == 1

if __name__ == '__main__':
    a = Solution()
    l = a.isHappy(2)
    print(l)