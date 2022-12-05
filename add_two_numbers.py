'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored 
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return 
the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

https://leetcode.com/problems/add-two-numbers/
'''

from typing import Optional
import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''Is correct but not expect solution'''
        
        a = ''.join(map(str,(l1[::-1])))
        b = ''.join(map(str,(l2[::-1])))
        result = [int(x) for x in str(int(a) + int(b))]        

        return result[::-1]




@pytest.mark.parametrize('l1, l2, result',[
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),
])
def test_add_two_numbers(l1, l2, result):
    assert Solution().addTwoNumbers(l1, l2) == result
