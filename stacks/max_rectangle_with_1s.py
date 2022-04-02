from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int], n) -> int:
            s = []
            res = 0
            for i in range(n):
                while s and heights[s[-1]] >= heights[i]:
                    tp = s.pop()
                    curr = heights[tp]*(i if not s else (i-s[-1]-1))
                    res = max(res, curr)
                s.append(i)
            while s:
                tp = s.pop()
                curr = heights[tp]*(n if not s else (n-s[-1]-1))
                res = max(res, curr)

            return res

        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(matrix[i][j])
        res = largestRectangleArea(matrix[0], c)

        for i in range(1, r):
            for j in range(c):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
            res = max(res, largestRectangleArea(matrix[i], c))
        return res
