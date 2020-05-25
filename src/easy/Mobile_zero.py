# 移动零

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        # 非0元素统计完了，剩下的都是0了
        # 所以第二次遍历把末尾的元素都赋为0即可
        for i in range(j, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    a = Solution()
    l = a.moveZeroes(None)
    print(l)