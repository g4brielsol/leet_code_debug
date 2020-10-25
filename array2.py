# 2 is even
# 3 is odd
class Solution:
    def findNumbers(self, nums: list) -> int:
        if (len(nums) >= 1) and (len(nums) <= 500):  
            even_digits = 0
            for number in nums:
                if (number >= 1) and (number <= 10**5):
                    digit_counter = 0
                    while(number != 0):
                        digit_counter += 1
                        number = number // 10
                    if digit_counter % 2 == 0:
                        even_digits += 1
                    else:
                        pass
                else:
                    return False
        else:
            return False

        return even_digits
    