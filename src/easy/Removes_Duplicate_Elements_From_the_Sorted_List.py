# 删除排序链表中的重复元素

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 双指针法 + 额外的空间
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return ListNode

        pi = ListNode(-999)
        pii = pi
        pj = head

        while pj.next:
            if pj.val != pi.val:
                pi.next = ListNode(pj.val)
                pi = pi.next
            pj = pj.next

        if pj.val != pi.val:
            pi.next = ListNode(pj.val)

        return pii.next

    # 双指针法
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head

        pi = head
        pii = pi
        pj = head

        while pj.next:
            pj = pj.next
            if pj.val != pi.val:
                pi.next = pj
                pi = pi.next

        if pj.val != pi.val:
            pi.next = pj

        pi.next = None  # 删除余下的链表部分

        return pii.next

if __name__ == '__main__':
    a = Solution()
    l = a.deleteDuplicates2([])
    print(l)