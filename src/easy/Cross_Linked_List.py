class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # 走的路程是一样的，总会相遇的！
    # 错的人迟早会走散，而对的人迟早会相逢！
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA