class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        # Your code here
        res = arr[0]
        maxEnding = arr[0]

        for i in range(1, N):
            maxEnding = max(maxEnding+arr[i], arr[i])
            res = max(res, maxEnding)

        return res
