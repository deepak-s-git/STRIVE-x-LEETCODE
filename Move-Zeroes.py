n = len(nums)
i = 0

for j in range(n):
    if (nums[j] != 0):      
        nums[i],nums[j] = nums[j],nums[i]   #SWAP TE I AND J DATA IN IF J IS IN NON ZERO ELEMENT
        i += 1