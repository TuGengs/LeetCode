# 杨辉三角 (每一项都对应着(a + b)的n次方展开后每一项的系数)

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rs = []
        if numRows == 0:
            return rs

        rs.append([1])

        for i in range(1, numRows):
            tmp = []
            for j in range(i + 1):  # 该行的列数
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(rs[i - 1][j - 1] + rs[i - 1][j])
            rs.append(tmp)

        return rs

if __name__ == '__main__':
    a = Solution()
    l = a.generate(5)
    print(l)