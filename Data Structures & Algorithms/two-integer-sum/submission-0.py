class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        value={}
        for i,j in enumerate(nums):
           diff=target-j
           if diff in value:
            return [value[diff],i]
           value[j]=i 
        
                




        