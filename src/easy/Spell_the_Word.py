# 拼写单词

class Solution:
    # hash表计数法
    def countCharacters(self, words, chars):
        """
        # :param words:   List[str]
        # :param chars:   str
        # :return:        int
        """
        import collections
        chars_cnt = collections.Counter(chars)

        nums = 0

        for word in words:
            word_cnt = collections.Counter(word)
            for w in word_cnt:
                if word_cnt[w] > chars_cnt[w]:
                    break
            else:
                nums += len(word)

        return nums

if __name__ == '__main__':
    a = Solution()
    l = a.countCharacters(["cat","bt","hat","tree"], "atach")
    print(l)
