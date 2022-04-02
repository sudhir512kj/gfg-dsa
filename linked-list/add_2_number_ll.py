# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        prev = None
        s1 = s2 = s3 = []

        while first:
            s1.append(first)
            first = first.next

        while second:
            s2.append(second)
            second = second.next

        carry = 0

        while s1 and s2:
            sum = s1[-1].data + s2[-1].data + carry
            temp = Node(sum % 10)

            s3.append(temp)
            print(s3[-1].data)
            if sum > 9:
                carry = 1
            else:
                carry = 0

            s1.pop()
            s2.pop()

        while s1:
            sum = s1[-1].data + carry
            temp = Node(sum % 10)

            s3.append(temp)
            print(s3[-1].data)
            if sum > 9:
                carry = 1
            else:
                carry = 0

            s1.pop()

        while s2:
            sum = s2[-1].data + carry
            temp = Node(sum % 10)

            s3.append(temp)
            print(s3[-1].data)
            if sum > 9:
                carry = 1
            else:
                carry = 0

            s2.pop()

        if carry == 1:
            temp = Node(1)
            s3.append(temp)

        if s3:
            prev = s3[-1]

        while s3:
            temp = s3[-1]
            s3.pop()

            if len(s3) == 0:
                temp.next = None
            else:
                temp.next = s3[-1]

        return prev
