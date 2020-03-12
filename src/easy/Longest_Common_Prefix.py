#  最长公共前缀
# way_1
# Bug 01    []
# Bug 02    ""  len("") 长度为0
# def longestCommonPrefix(self, strs) -> str:
#     lens = len(strs)
#     flag = True
#     i = 0  # 位置
#     if lens == 0:
#         return ""
#     if lens == 1:
#         return strs[0]
#     while flag:
#         s = set()
#         for id in range(lens):  # 字符串id
#             if len(strs[id]) == 0:
#                 return ""
#             if len(strs[id]) > i:
#                 s.add(strs[id][i])
#             else:
#                 return strs[0][0: i]
#         if i == 0 and len(s) > 1:
#             return ""
#         if len(s) != 1:
#             return strs[0][0: i]
#         if len(s) == 1:
#             i += 1
################################################################
# way_2 水平扫描法
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        s = strs[0] # flower
        for i in range(1, len(strs)):
            while strs[i][:len(s)] != s:
                s = s[:-1]
        return s
 
if __name__ == '__main__':
    a = Solution()
    l = a.longestCommonPrefix(["flower","flow","flight"])
    print(l)