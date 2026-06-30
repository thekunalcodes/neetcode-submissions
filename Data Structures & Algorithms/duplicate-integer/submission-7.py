class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        n=len(nums)

        
        for j in range(1,n):
            if nums[j]==nums[j-1]:
                return True
            
            j+=1
        return False
                
            
            
        

        
        
        

        
            

        