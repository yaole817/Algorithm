"""
Describe:
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        if l1.val > l2.val:
            l2 = l2.next
            current = l2
        else:
            current = l1
            l1 = l1.next
        while l1 != None or l2 != None: 
            if l1 == None or l1.val > l2.val:
                current.next = l2
                current = current.next
                l2 = l2.next           
            elif l2 == None or l1.val <= l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
        return head


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(6)
    n3 = ListNode(8)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(2)
    m2 = ListNode(5)
    m3 = ListNode(9)
    m1.next = m2
    m2.next = m3

    s = Solution()
    r = s.mergeTwoLists(n1, m1)
    while r != None:
        print(r.val)
        r = r.next
    

    