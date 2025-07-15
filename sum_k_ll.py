# Definition for singly-linked list.
from typing import List, Optional
from heapq import heappush, heappop



class ListNode:
     def __init__(self, val=0, nex=None):
         self.val = val
         self.next = nex

     def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + '->' + str(self.next)
     def __repr__(self):
        return str(self.val)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for ll in lists:
            while ll:
                heappush(heap, ll.val)
                ll = ll.next
        out =None
        curr = None
        for i in range(len(heap)):
            if out is None:
                out = ListNode(heappop(heap))
                curr = out
            else:
                curr.next = ListNode(heappop(heap))
                curr = curr.next
        return out
if __name__ == "__main__":
    def lst_to_nodelist(lst):
        out=None
        current_node = None

        for num in lst:
            if out is None:
                out = ListNode(num)
                current_node = out
            else:
                current_node.next = ListNode(num)
                current_node = current_node.next
        if not out:
            out = []
        return out
    test1 = [[1,4,5],[1,3,4],[2,6]]
    inp = [lst_to_nodelist(x) for x in test1]
    print(Solution().mergeKLists(inp))
    print(Solution().mergeKLists([]))
    print(Solution().mergeKLists([[]]))