class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check if matrix is empty 
        if not matrix:
            return False
        row= len(matrix)
        column = len(matrix[0])
        high = row * column -1
        low = 0
        
        # perform binary search
        while low <= high:
            mid = (low+high)//2
            mid_value = matrix[mid//column][mid%column]
            
            if target == mid_value:
                return True
            elif mid_value < target:
                low = mid+1
            else:
                high = mid-1
            
        return False
        