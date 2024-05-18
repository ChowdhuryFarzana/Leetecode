class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # initializing variable k to 0
        k = 0
        # loop through each element in nums
        for i in range(len(nums)):
            #checking if current element is in val
            if nums[i] != val:
                # if it is not equal, then we store it in k
                nums[k] = nums[i]
                # Increment 'k' to move to the next position
                k+=1
        return k 