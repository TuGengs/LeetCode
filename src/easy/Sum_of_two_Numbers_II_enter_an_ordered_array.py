# 两数之和 II - 输入有序数组

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        pi = 0
        pj = len(numbers) - 1

        while pi < pj:
            if target == numbers[pi] + numbers[pj]:
                return [pi + 1, pj + 1]
            elif target < numbers[pi] + numbers[pj]:
                pj -= 1
            else:
                pi += 1


if __name__ == '__main__':
    a = Solution()
    l = a.twoSum([2, 7, 11, 15], 9)
    print(l)