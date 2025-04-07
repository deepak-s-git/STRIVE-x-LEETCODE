class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
     count = {}
     for num in nums:
        if num in count:
            return num
        else:
            count[num] = 1   # Initialize the count for the number