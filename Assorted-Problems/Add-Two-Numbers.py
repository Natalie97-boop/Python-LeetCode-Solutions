# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_out = 0
        head_pointer = None
        temp_head = ListNode()
        node_sum = 0
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1 is None and l2 is None:
            return None

        while l1 or l2:
            
            node_sum += carry_out

            if l1:
                node_sum += l1.val
                l1 = l1.next
                
            if l2:
                node_sum += l2.val
                l2 = l2.next

            bit_sum = node_sum % 10
            
            carry_out = 0
        
            if (node_sum >= 10):
                carry_out = 1

            if head_pointer is None:
                head_pointer = temp_head
                head_pointer.val = bit_sum
            else:
                head_pointer.next = ListNode()
                head_pointer = head_pointer.next
                head_pointer.val = bit_sum

            node_sum = 0
            
        if carry_out == 1:
            head_pointer.next = ListNode(carry_out)

        return temp_head
