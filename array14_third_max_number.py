#Given a non-empty array of integers, return the third maximum number in this array. 
#If it does not exist, return the maximum number. The time complexity must be in O(n).

class Solution:
    def thirdMax(self, nums: list) -> int:
        if len(nums) > 0:
            if len(nums) < 3:
                return self.three_values(nums)[0]
            else:
                iterator = 1
                size = len(nums)
                while iterator < size:
                    # is a repeated number
                    if nums[iterator] in nums[:iterator]:
                        nums = nums[:iterator] + nums[iterator+1:]
                        size -= 1
                        iterator -= 1
                    iterator += 1
        #print(nums)
        if len(nums) > 2:
            return self.three_values(nums)[2]
        else:
            return self.three_values(nums)[0]
        

    def three_values(self, array: list) -> list:
        one = -(10**23)
        two = -(10**23)
        three = -(10**23)
        for element in array:
            if element > one:
                three = two
                two = one
                one = element
            if (element < one) and (element > two):
                three = two
                two = element
            if (element < two) and (element > three):
                three = element
        #[1,2,-2147483648]
        return [one, two, three]

        #[1,2,-2147483648]
        #[1,2,2,5,3,5]
        #[1,2,5,3]
        
        #3 = 0
        #2 = 1
        #1 = 2
    
        #[0,0,0,0]
        #[0,0,0]
        #[0,0]
        #[0]
        
        #[1,2,3] # len 3