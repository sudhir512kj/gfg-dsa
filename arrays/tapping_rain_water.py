class Solution:
    def trappingWater(self, arr, n):
        # Code here
        res = 0
        lmax, rmax = [None]*n, [None]*n

        lmax[0] = arr[0]
        for i in range(1, n):
            lmax[i] = max(arr[i], lmax[i-1])

        rmax[n-1] = arr[n-1]
        for i in range(n-2, 0, -1):
            rmax[i] = max(arr[i], rmax[i+1])

        for i in range(1, n-1):
            res += (min(lmax[i], rmax[i])-arr[i])

        return res
