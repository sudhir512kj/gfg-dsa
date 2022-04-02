def missingsmallestpositive(arr):
    arr.sort()
    ans = 1
    for i in range(len(arr)):
        if arr[i] == ans:
            ans += 1
    return ans