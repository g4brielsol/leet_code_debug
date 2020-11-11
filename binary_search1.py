import time

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if ((dividend >= -(2**31)) and (dividend <= (2**31) - 1)) or (divisor >= (divisor <= (2**31) - 1)):
            negative_numbers = 0
            if (dividend < 0):
                dividend = dividend * (-1)
                negative_numbers += 1
            if (divisor < 0):
                divisor = divisor * (-1)
                negative_numbers += 1
            if (divisor == 0):
                return False
            quotient = 0
            division_sum = 0
            while (division_sum + divisor <= dividend):
                division_sum += divisor
                quotient += 1    
            if negative_numbers == 1:
                return -quotient
            else:
                return quotient
        else:
            return (2**31) - 1 

sol = Solution()
inicio = time.time()
sol.divide(-2147483648, -1)
print(time.time() - inicio)