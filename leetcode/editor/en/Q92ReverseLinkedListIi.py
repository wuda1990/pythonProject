# -*- coding: UTF-8 -*-
# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position 
# right, and return the reversed list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [5], left = 1, right = 1
# Output: [5]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is n. 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# Follow up: Could you do it in one pass?
# 
#  Related Topics Linked List 👍 8352 👎 370


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# other solution
# #https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for i in range(1, left):
            pre = pre.next
        middle_head = pre
        p = pre.next
        q = p.next
        for i in range(left, right):
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        middle_head.next.next = q
        middle_head.next = p
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.reverseBetween(l, 2, 4)

# leetcode submit region end(Prohibit modification and deletion)
