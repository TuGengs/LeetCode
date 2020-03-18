# 矩形重叠

class Solution:
    # 检查位置
    # 如果我们在平面中放置一个固定的矩形 rec2，那么矩形 rec1 必须要出现在 rec2 的「四周」，
    # 也就是说，矩形 rec1 需要满足以下四种情况中的至少一种：
    # 矩形 rec1 在矩形 rec2 的左侧；rec1[2] <= rec2[0]
    # 矩形 rec1 在矩形 rec2 的右侧；rec1[0] >= rec2[2]
    # 矩形 rec1 在矩形 rec2 的上方；rec1[1] >= rec2[3]
    # 矩形 rec1 在矩形 rec2 的下方。rec1[3] <= rec2[1]
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top
    # 检查区域
    # 如果两个矩形重叠，那么它们重叠的区域一定也是一个矩形，
    # 那么这代表了两个矩形与 xx 轴平行的边（水平边）投影到 xx 轴上时会有交集，
    # 与 yy 轴平行的边（竖直边）投影到 yy 轴上时也会有交集。
    # 因此，我们可以将问题看作一维线段是否有交集的问题。
    # 当 min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])   X
    # 当 min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])   Y
    def isRectangleOverlap2(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        return  min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and \
                    min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])

if __name__ == '__main__':
    a = Solution()
    l = a.isRectangleOverlap2([0,0,1,1], [1,0,2,1])
    print(l)