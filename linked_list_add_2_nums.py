# This is a sample Python script.
from typing import Optional


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __len__(self):
        if self.next:
            return 1 + len(self.next)
        else:
            return 1

    def __str__(self):
        out = []
        lst = self
        while lst:
            out.append(lst.val)
            lst = lst.next
        return str(out)


class Solution:

    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        len_l1 = len(l1)
        len_l2 = len(l2)
        len_max, len_min = (len_l1, len_l2) if len_l1 >= len_l2 else (len_l2, len_l1)
        if len_l1 < len_l2:
            l2, l1 = l1, l2

        out = ListNode()
        carry = 0
        out_temp = out
        for ii in range(len_max):
            if l2:
                val = (l1.val + l2.val + carry)
            else:
                val = (l1.val + carry)
            out_temp.val = val % 10
            carry = 1 if val > 9 else 0
            l1 = l1.next
            if l2:
                l2 = l2.next
            if ii != (len_max -1):
                out_temp.next = ListNode()
                out_temp = out_temp.next
        if carry:
            out_temp.next = ListNode(1)
        return out


if __name__ == "__main__":
    l1t = ListNode(2)
    l1t.next = ListNode(4)
    l1t.next.next = ListNode(5)

    l2t = ListNode(5)
    l2t.next = ListNode(6)
    l2t.next.next = ListNode(4)

    sum_ = Solution.add_two_numbers(l1t, l2t)

    print(sum_)
