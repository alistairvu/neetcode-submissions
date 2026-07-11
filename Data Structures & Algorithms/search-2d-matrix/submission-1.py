class Solution:
    def findRow(self, matrix: list[list[int]], target: int) -> int:
        left, right = 0, len(matrix) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False