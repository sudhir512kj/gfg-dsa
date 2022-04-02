def insert(stack, x):
    # code here
    stack.append(x)

# Function to remove top element from stack.


def remove(stack):
    # code here
    return stack.pop()

# Function to print the top element of stack.


def headOf_Stack(stack):
    # code here
    return stack[-1]

# Function to search an element in the stack.


def find(stack, x):
    # code here
    if x in stack:
        return True
    return False
