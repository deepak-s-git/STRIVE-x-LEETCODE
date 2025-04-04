class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
     
     n = len(nums)
     i = 0
     for j in range(n):
        if (nums[j] != 0):
            nums[i],nums[j] = nums[j],nums[i]    #SWAP I AND J IF J IS IN NON ZERO ELEMENT
            i += 1