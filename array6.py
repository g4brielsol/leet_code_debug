# remove item from list without making list copy

import copy
class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        nums = copy.copy(nums)
        size = len(nums)
        if ((size >= 0) and (size <= 10000)) and ((val >= 0) and (val <= 100)):
            counter = 0
            while counter < size:
                if (nums[counter] >= 0) and (nums[counter] <= 50):
                    if nums[counter] == val:
                        nums = nums[:counter] + nums[counter + 1:]
                        size -= 1
                        counter -= 1
                    counter += 1
                else:
                    return False
        else:
            return False
        print(nums)
        return len(nums)#("{}, nums = {}".format(len(nums), nums))
            
        # tests
        
        #[0,1,2,3,2,4,5] val = 2
        #[0,1,3,2,4,5]
        #[0,1,3,4,5]
        
        
        #[0,0,0,0] val = 0
        #[0,0,0]
        #[0,0]
        #[0]
        
        #[1,0,1,0,0,1] val = 1