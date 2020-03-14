# 搜索插入位置

class Solution:
    # 顺序查找法
    def searchInsert(self, nums, target):

        """
        :param nums:    List[int]
        :param target:  int
        :return:        int
        """

        for i in range(len(nums)):
            if nums[i] >= target:
                nums.insert(i, target)
                return i
        nums.insert(len(nums) - 1, target)
        return len(nums) - 1

    # 折半查找发
    def searchInsert2(self, nums, target):

        """
        :param nums:    List[int]
        :param target:  int
        :return:        int
        """

        left = 0
        right = len(nums) - 1

        # 特例
        if target > nums[right]:
            return right + 1

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    a = Solution()
    l = a.searchInsert2([1,3,5,6], 0)
    print(l)
    l2 = a.searchInsert2([1,3,5,6], 7)
    print(l2)