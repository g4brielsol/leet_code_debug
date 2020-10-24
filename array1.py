class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        counter = 0
        max_counter = 0
        for item in nums:
            if item == 1:
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            else:
                counter = 0
        
        return max_counter

instantiate =  Solution()
instantiate.findMaxConsecutiveOnes([1,0,1,1,0,1])