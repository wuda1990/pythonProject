# -*- coding: UTF-8 -*-
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 栈 递归 链表 双指针 👍 1154 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import collections


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        pre = None
        # 反转mid后面的节点
        while mid is not None:
            q = mid.next
            mid.next = pre
            pre = mid
            mid = q

        mid = pre
        p = head
        while p != mid and mid is not None:
            if p.val != mid.val:
                return False
            p = p.next
            mid = mid.next
        parent = collections.defaultdict(list)
        return True


solution = Solution()
p1 = ListNode(1)
p2 = ListNode(2)
# p3 = ListNode(2)
# p4 = ListNode(1)
p1.next = p2
# p2.next = p3
# p3.next = p4
result = solution.isPalindrome(p1)
print (result)

# leetcode submit region end(Prohibit modification and deletion)
