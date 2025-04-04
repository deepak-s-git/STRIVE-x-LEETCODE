class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        #RETURNS THE MINIMUM NUMBER OF UNIQUE CANDIESWHICH SHE CAN EAT 
        return int(min(len(candyType)/2,len(set(candyType))))