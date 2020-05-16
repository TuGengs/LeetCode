# 旋转数组

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        tmpl = len(nums)

        k %= tmpl

        nums2 = nums[:tmpl - k]
        nums1 = nums[tmpl - k :]

        tmp = nums1 + nums2
        nums[:] = tmp[:]
        print(nums)

if __name__ == '__main__':
    a = Solution()
    l = a.rotate([1,2,3,4,5,6,7], 3)