class Solution:
    def searchMatrix(self, matrix, target):
        top = 0
        bottle = len(matrix) - 1
        while top <= bottle:
            medium = (top + bottle) // 2
            if matrix[medium][-1] < target:
                top = medium + 1
            elif matrix[medium][0] > target:
                bottle = medium - 1
            else:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    med = (left + right) // 2
                    if matrix[medium][med] < target:
                        left = med + 1
                    elif matrix[medium][med] > target:
                        right = med - 1
                    else:
                        return True
                return False
        return False
                     

x = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(x.searchMatrix(matrix, target))
