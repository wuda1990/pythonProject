# -*- coding: UTF-8 -*-
# Given the head of a linked list, remove the nᵗʰ node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
# 
#  Related Topics Linked List Two Pointers 👍 13980 👎 578


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        first = dummy
        for _ in range(n):
            first = first.next
        second = dummy
        while first.next:
            first = first.next
            second = second.next
        # remove
        second.next = second.next.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
