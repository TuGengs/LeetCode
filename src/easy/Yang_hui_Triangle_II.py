# 杨辉三角 II  (每一项都对应着(a + b)的n次方展开后每一项的系数)

# （a＋b）^n
# =a^n+C(n,1)a^(n-1)b
# + C(n,2)a^(n-2)b^2
# +C(n,3)a^(n-3)b^3
# +……+C(n,n-2)a^2b^(n-2)+C(n,n-1)ab^(n-1)+b^n

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        result = [0] * (rowIndex + 1)

        for index in range(rowIndex + 1):
            if index == 0:
                result[0] = 1
            elif index == 1:
                result[1] = rowIndex
            elif index <= (rowIndex) / 2:   # 对称的
                result[index] = result[index - 1] * (rowIndex - index + 1) / index
            else:
                result[index] = result[rowIndex - index]

        return result

if __name__ == '__main__':
    a = Solution()
    l = a.getRow(5)
    print(l)