class Solution:

    # Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self, s):
        # code here
        st = []
        for each in s:
            if st and st[-1] == each:
                pass
            else:
                st.append(each)
        return "".join(st)
