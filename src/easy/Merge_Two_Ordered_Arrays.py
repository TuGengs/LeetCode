# 合并两个有序数组

class Solution:
    # 双指针法，无需额外的空间
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) == 0:
            return n
        if len(nums2) == 0:
            return m

        pi = 0  # < m + n
        pj = 0  # < n
        d = 0

        while pi < m + n and pj < n:
            if nums1[pi] >= nums2[pj]:
                nums1.insert(pi, nums2[pj])
                d += 1
                pj += 1
            if nums1[pi] == 0 and pi >= m + d:
                nums1.insert(pi, nums2[pj])
                d += 1
                pj += 1
            pi += 1

        del nums1[m + n:]

    # 双指针法，额外的空间
    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) == 0:
            return n
        if len(nums2) == 0:
            return m

        ns = []
        pi = 0
        pj = 0

        while len(ns) < m + n:
            if pj < n and (nums2[pj] <= nums1[pi]):
                ns.append(nums2[pj])
                pj += 1
            else:
                if pi < m:
                    ns.append(nums1[pi])
                    pi += 1
                else:
                    ns.append(nums2[pj])
                    pj += 1

        nums1[:] = ns[:]

if __name__ == '__main__':
    a = Solution()
    l = a.merge2([2,0], 1, [1], 1)
    print(l)