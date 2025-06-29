from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_head = None
        result_tail = result_head
        rest = 0
        while l1 and l2:
            tmp = l1.val + l2.val + rest
            if tmp >= 10:
                tmp -= 10
                rest = 1
            else:
                rest = 0
            if not result_head:
                result_head = ListNode(tmp, None)
                result_tail = result_head
            else:
                result_tail.next = ListNode(tmp, None)
                result_tail = result_tail.next
            l1 = l1.next
            l2 = l2.next
        remaining = l2
        if l1:
            remaining = l1
        while remaining:
            tmp = remaining.val + rest
            if tmp >= 10:
                tmp -= 10
                rest = 1
            else:
                rest = 0
            result_tail.next = ListNode(tmp, None)
            result_tail = result_tail.next
            remaining = remaining.next
        if rest != 0:
            result_tail.next = ListNode(rest, None)
        return result_head
