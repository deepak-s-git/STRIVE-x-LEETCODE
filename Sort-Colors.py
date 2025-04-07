class Solution:
    def sortColors(self, nums: List[int]) -> None:

        red = 0
        white = 0              #3 POINTER APPROACH
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white],nums[red] = nums[red],nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:   #
                white += 1
            else:
                nums[white],nums[blue] = nums[blue],nums[white]    #SWAPS WITH POINTER BLUE IF WHITE IS AT POSITION HAVING NUMBER 2(BLUE)
                blue -= 1