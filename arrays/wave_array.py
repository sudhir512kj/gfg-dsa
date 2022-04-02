class Solution:
    # Complete this function
    # Function to sort the array into a wave-like array.
    def convertToWave(self, arr, N):
        # Your code here
        for i in range(0, N, 2):

            # If current even element is smaller than previous
            if (i > 0 and arr[i] < arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]

            # If current even element is smaller than next
            if (i < N-1 and arr[i] < arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
