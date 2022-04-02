class Solution:

    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram):
        # code here
        st = []
        res = 0
        n = len(histogram)

        for i in range(n):
            while st and histogram[st[-1]] >= histogram[i]:
                tp = st.pop()
                curr = histogram[tp] * (i if not st else (i-st[-1]-1))
                res = max(res, curr)
            st.append(i)

        while st:
            tp = st.pop()
            curr = histogram[tp] * (n if not st else (n-st[-1]-1))
            res = max(res, curr)
        return res
