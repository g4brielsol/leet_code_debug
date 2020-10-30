# Given an array of integers A sorted in non-decreasing order, 
# return an array of the squares of each number, also in sorted non-decreasing order.

# nao sei se acertei
class Solution:
    def sortedSquares(self, A: list) -> list:
        if (len(A) >= 1) and (len(A) <= 10000):
            for index in range(0, len(A)):
                if (A[index] >= -10000) and (A[index] <= 10000):
                    A[index] = (A[index]) ** 2
            
            return(self.counting_sort(A))
    
    
    def counting_sort(self, A: list) -> list:
        min_value = A[0]
        max_value = A[-1]
        for element in A:
            if element > max_value:
                max_value = element
            if element < min_value:
                min_value = element
                
        max_value = max_value - min_value
            
        count = [0 for i in range(max_value + 1)]
        
        for i in A:
            count[i - min_value] += 1
            
        index = 0
        for i in range(max_value + 1):
            for j in range(count[i]):
                A[index] += i + min_value
                index += 1
        return A
                
                
#[1,2,3,4,5]
#[1,4,9,16,25]