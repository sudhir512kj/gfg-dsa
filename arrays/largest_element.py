class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, sizeOfArray, arr):

        # Your code here'''
        # Function should return a list containing two elements'''
        # li = [maximum, second_maximum]
        res = -1
        largest = 0

        for i in range(1, sizeOfArray):
            if arr[i] > arr[largest]:
                res = largest
                largest = i
            elif arr[i] != arr[largest]:
                if res == -1 or arr[i] > arr[res]:
                    res = i

        if arr[res] == arr[largest]:
            return [arr[largest], -1]
        return [arr[largest], arr[res]]
