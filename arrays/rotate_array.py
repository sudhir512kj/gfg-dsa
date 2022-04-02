class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, A, D, N):
        # Your code here
        temp = [None]*D
        for i in range(D):
            temp[i] = A[i]

        for i in range(D, N):
            A[i-D] = A[i]

        for i in range(D):
            A[N-D+i] = temp[i]

        return A
