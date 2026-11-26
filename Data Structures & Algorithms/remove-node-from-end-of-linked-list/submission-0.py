# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ll = 0 
        counter = 0
        curr, curr2 = head, head
        while curr is not None:
            len_ll += 1
            curr = curr.next
        pos = (len_ll - n) + 1

        print(len_ll)
        print(pos)
        print(curr2.val)

        if (pos == 1):
            return head.next

        while curr2 is not None: 
            counter += 1
            if counter == pos-1:
                curr2.next = curr2.next.next
                break
            else: 
                curr2 = curr2.next

        return head