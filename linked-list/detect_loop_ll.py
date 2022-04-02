# User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''


class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        slow_p = head
        fast_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                return True
        return False
