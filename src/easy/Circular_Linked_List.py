# 环形链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        pk = head.next
        pm = head

        while pk != pm:
            if not pk or not pk.next:
                return False
            else:
                pk = pk.next.next
                pm = pm.next

        return True

if __name__ == '__main__':
    a = Solution()
    l = a.hasCycle(None)
    print(l)