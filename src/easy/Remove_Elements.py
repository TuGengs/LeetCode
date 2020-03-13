# 移除元素 与 删除排序数组中的重复项 雷同

class Solution:
    def removeElement(self, nums, val) -> int:

        """
        :param nums:    List[int]
        :param val:     int
        :return:        int
        """
        p1 = 0
        for p2v in nums:
            if p2v != val:
                nums[p1] = p2v
                p1 += 1
        del nums[p1:]
        return len(nums)

if __name__ == '__main__':
    a = Solution()
    l = a.removeElement([1, 2, 3, 4, 8], 2)
    print(l)