# User function Template for python3

class Solution:
    def matching(self, a, b):
        return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # code here
        st = []
        for each in x:
            if each == '(' or each == '{' or each == '[':
                st.append(each)
            else:
                if not st:
                    return False
                if not self.matching(st[-1], each):
                    return False
                else:
                    st.pop()
        return len(st) == 0
