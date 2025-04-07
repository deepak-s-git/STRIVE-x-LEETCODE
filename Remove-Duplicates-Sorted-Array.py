class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:     #IF THE CURRENT ELEMENT IS NOT EQUAL TO PREVIOUS ONE
                nums[j] = nums[i]          #THEN ITS A NEW UNIQUE ELEMENT...PUT IT IN PLACE OF J
                j += 1

        return j       #LENGTH OF THE UNIQUE ELEMENT ARRAY