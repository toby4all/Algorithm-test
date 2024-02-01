#!/usr/bin/env python3

class Solution:
    def solution(self, A):
        num_countries = 0
        stack = []

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != -1:
                    stack.append((i, j))
                    num_countries += 1
                    self.dfs(A, stack, A[i][j])
                    stack = []

        return num_countries

    def dfs(self, A, stack, color):
        while stack:
            i, j = stack.pop()
            if 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == color:
                A[i][j] = -1  # Mark as visited
                stack.append((i + 1, j))
                stack.append((i - 1, j))
                stack.append((i, j + 1))
                stack.append((i, j - 1))


# Test the function with the given example
A = [
    [5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]
]
solution = Solution()
print(solution.solution(A))  # Output: 11
