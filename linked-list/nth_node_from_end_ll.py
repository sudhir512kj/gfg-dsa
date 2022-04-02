# User function Template for python3
'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
# Function to find the data of nth node from the end of a linked list


def getNthFromLast(head, n):
    # code here
    if not head:
        return -1
    first = head
    for i in range(n):
        if not first:
            return -1
        first = first.next

    second = head
    while first:
        second = second.next
        first = first.next

    return second.data
