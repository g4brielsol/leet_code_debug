#Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

#class Solution:
#    def maxSubArray(self, nums: List[int]) -> int:
class Solution:
    def maxSubArray(self, nums: list) -> list:
        if (len(nums) >= 1) and (len(nums) <= 2 * (10**4)):
            biggest_sum = -(2**31)
            #        len(nums) = 5,  0 <= i <= 4
            for i in range(0, len(nums)):
                if (nums[i] >= -(2**31)) and (nums[i] <= (2**31) - 1):
                    for j in range(i+1, len(nums) + 1):
                        if sum(nums[i:j]) > biggest_sum:
                            biggest_sum = sum(nums[i:j])
            return biggest_sum #nums[i:j]
       