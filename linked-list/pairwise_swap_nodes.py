# User function Template for python3
'''
	Your task is to pairwise nodes of 
	the given linked list.
	
	Function Arguments: head of the original list.
	Return Type: reference to head of the given linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
# Function to swap elements pairwise.


def pairwiseSwap(head):
    # code here
    curr = head
    while curr and curr.next:
        curr.data, curr.next.data = curr.next.data, curr.data
        curr = curr.next.next
    return head
