# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #Find mid-point by using slow and fast 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        #Reverse the second list
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev

        #Merge first and second reveresed list
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next     # simpan dulu
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2