class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hash_Map = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]   #CALCULATE THE OTHER NUMBER REQUIRED WITH NUMS[I] YP ADD UP TO TARGET
            if comp in Hash_Map:
                return [Hash_Map[comp] , i]      #IF THE OTHER VALUE IS IN HASHMAP IT RETURNS THE INDICES OF BOTH THE NUMBERS
            Hash_Map[nums[i]] = i
        
        return []  