def maximumAdjacent(sizeOfArray, arr):

    # Your code here
    # Function should print max of all adjacents
    for i in range(1, sizeOfArray):
        print("{}".format(max(arr[i], arr[i-1])), end=" ")
