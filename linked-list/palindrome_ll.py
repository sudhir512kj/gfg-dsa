# User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
# Function to check whether the list is palindrome.


class Solution:
    def reverseLL(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def isPalindrome(self, head):
        # code here
        if not head:
            return True
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        rev = self.reverseLL(slow.next)
        curr = head

        while rev:
            if rev.data != curr.data:
                return False
            rev = rev.next
            curr = curr.next

        return True
