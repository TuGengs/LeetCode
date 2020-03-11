#将数组分成和相等的三个部分
# way1 the following
# sum(List) / 3 -> the value of each list -> list nums = 3? true : no
class Solution:
    def canThreePartsEqualSum(self, A):
        amount = sum(A)
        single = amount / 3
        if single % 1 == 0:
            s = 0
            l = []
            for i in range(len(A)):
                s += A[i]
                if s == single:
                    l.append(s)  # 第一段求出后,加入数组,和清零
                    s = 0
                    if len(l) == 2 and i < len(A) - 1:  # 求出前两部分和后,求第三部分     超出索引求和为0,我也不知道
                        c = sum(A[i + 1:])
                        l.append(c)
                        return l[1] == l[0] == l[2]
        return False
if __name__ == '__main__':
    a = Solution()
    l = a.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
    print(l)