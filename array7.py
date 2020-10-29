# remove duplicates
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if (len(nums) >= 0) and (len(nums) <= 3*(10**4)):
            i = 0
            size_array = len(nums)
            while i < size_array:
                if (nums[i] >= -(10**4)) and (nums[i] <= 10**4):
                    #repeat number
                    if nums[i] in nums[:i]:
                        nums = nums[:i] + nums[i+1:]
                        size_array -= 1
                        i -= 1
                    i += 1
        print(nums)
        return len(nums)
                        
                        
                        
                        
    
solution = Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
solution.removeDuplicates([0,0,0,0,1,1,2,2,3,3])
      #[0,1,2,3,4] size 6
#index  0 1 2 3 4  
    
    #[0,0,1,2,3,3,4]
    #result -> [0,1,2,3,4]