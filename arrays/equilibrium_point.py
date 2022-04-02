class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        total_sum = sum(A)
        leftsum = 0
        for i, num in enumerate(A):
            total_sum -= num

            if leftsum == total_sum:
                return i+1
            leftsum += num

        return -1
