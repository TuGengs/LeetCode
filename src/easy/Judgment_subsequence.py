# 判断子序列

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str    子序列
        :type t: str    母序列
        :rtype: bool
        """
        # 构建t的哈希集合
        hash_set = {}
        for i, word in enumerate(t):
            if word not in hash_set:
                hash_set[word] = [i]
            else:
                hash_set[word].append(i)

        # 匹配
        index = -1
        for word in s:
            if word not in hash_set:
                return False

            # 字母s出现的索引 用二分法找到其中大于index的第一个
            indexes = hash_set[word]
            left = 0
            right = len(indexes)
            while left < right:
                mid = left + (right - left) // 2
                if indexes[mid] > index:
                    right = mid
                else:
                    left = mid + 1
            if left == len(indexes):
                return False
            index = indexes[left]

            # indexes = hash_set[word]
            # print(indexes)
            # if indexes[0] < index:
            #     return False
            # index = indexes[0]

        return True

if __name__ == '__main__':
    a = Solution()
    l = a.isSubsequence("aaaaaa", "bbaaaa")
    print(l)