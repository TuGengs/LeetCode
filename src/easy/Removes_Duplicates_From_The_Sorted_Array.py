# 删除排序数组中的重复项

class Solution:
    # way_1 用集合的方法
    def removeDuplicates(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        l = list(set(nums))
        l.sort(key = nums.index)
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)

    # way_2 （双指针法）由于nums是有序的，所以从i=0开始，寻找与nums[i]不等于的数k，然后num[i+1]=k, i++，再继续从数k开始找
    # 综上，第一位永远对的，寻找与上一位不一样的添加进来，最后删除多余数组。
    def removeDuplicates2(self, nums):
        p1 = 0
        for p2v in nums:
            print(nums)
            if p2v != nums[p1]:
                p1 += 1
                nums[p1] = p2v
        del nums[p1 + 1:]
        return len(nums)

if __name__ == '__main__':
    a = Solution()
    l = a.removeDuplicates2([-1,0,0,0,1,3,3])
    print(l)