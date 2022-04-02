# function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
