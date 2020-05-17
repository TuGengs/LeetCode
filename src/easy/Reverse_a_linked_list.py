# 反转链表

class Solution:

    # 迭代法 (递归法比较复杂，而且空间复杂度为o(n))
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

if __name__ == '__main__':
    a = Solution()
    l = a.reverseList(None)
    print(l)