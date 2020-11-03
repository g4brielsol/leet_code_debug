#Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

#ou can return the answer in any order.

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dict_sum = {}
        for i in range(0, len(nums)):
            if nums[i] in dict_sum.keys():
                return [i, dict_sum[nums[i]]]
            else:
                dict_sum[target - nums[i]] = i
            
                        
        return []
        #[2,7,8,4,5] 7
        
    
        #[5] = 0
        
        #[0] = 1
        
        #[-1] = 2
        
        #[3] = 3