# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for element in range(1, len(nums) + 1):
            if element not in nums:
                nums = nums + [element]
        return nums[size:]
        
        
        
        # [1,2,3,4,5,6] []
        
#[1,2,2,5,5,5] len = 6    [3,4,6]
#[1,2,3,4,5,6,7,8] len = 8 []
#[1,1,1,1,1,1,1,8] len = 8  [2,3,4,5,6,7]  [1,2,3,4,5,6,7,8]
#[1,2,3,4,5,6,7,8]
#[1,1,1,1,1] len = 5        [2,3,4,5]
#[1,2,3,4,5]
#[1]         len = 1               []