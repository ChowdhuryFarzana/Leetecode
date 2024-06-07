class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
         # Initialize the position where the next unique or allowed duplicate element will be placed
          i = 1
    # Count how many times the current number has appeared
          count = 1
    
          for j in range(1, len(nums)):
              if nums[j] == nums[j - 1]:
                  count += 1
              else:
                   count = 1
        
              if count <= 2:
                 nums[i] = nums[j]
                 i += 1
    
          return i
                
                    
            
        