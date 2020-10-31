#Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.

#You may return any answer array that satisfies this condition.



class Solution:
    def sortArrayByParity(self, A: list) -> list:
        # 2 is even
        # 3 is odd
        if (len(A) >= 1) and (len(A) <= 5000):
            sorted_array = []
            for element in A:
                if (element >= 0) and (element <= 5000):
                    # even number
                    if element % 2 == 0:
                        sorted_array = [element] + sorted_array
                    else:
                        sorted_array = sorted_array + [element]
                            
        return sorted_array