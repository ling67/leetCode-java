"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
 
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#version1: stack
#version2:reverse

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []
        
        #一边走一边存入栈
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
           
        if fast:
            slow = slow.next
            
        while slow:
            top = stack.pop()
            
            if top != slow.val:
                return False
            slow = slow.next
        
        return True

       
#version2:reverse
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, curr, fast = None, head, head
        
        while fast and fast.next:
            fast = fast.next.next

            #reverse the left part of the linked list
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
                
        if not fast:        # even number of nodes
            left, right = prev, curr
        else:               # odd number of nodes
            left, right = prev, curr.next
        
        #compare
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
