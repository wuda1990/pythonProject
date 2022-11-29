# -*- coding: UTF-8 -*-
# Given a positive integer n, generate an n x n matrix filled with elements 
# from 1 to n² in spiral order. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  
# 
#  Related Topics Array Matrix Simulation 👍 4333 👎 199


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A, lo = [[n * n]], n * n
        while (lo > 1):
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(zip(*A[::-1]))
        return A

    def generateMatrix2(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.generateMatrix(3)
    print(res)
