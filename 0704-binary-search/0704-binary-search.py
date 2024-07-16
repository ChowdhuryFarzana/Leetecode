class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        
        while low <= high:
            mid = (high + low)//2
            mid_val =  nums[mid]
            
            if target == mid_val:
                return mid
            elif mid_val < target:
                    low = mid+1
            else:
                high = mid -1
        return -1
                    
                
        
        