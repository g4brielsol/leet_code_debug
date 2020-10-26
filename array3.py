class Solution:
    def merge_sort(self, array: list) -> list:
        if len(array) > 1:
            middle = len(array) // 2
            left = array[:middle]
            right = array[middle:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array
    
    def sortedSquares(self, A: list) -> list:
        if (len(A) >= 1) and (len(A) <= 10000):
            for number in range(0, len(A)):
                if (A[number] >= -10000) and (A[number] <= 10000):
                    A[number] = (A[number]) ** 2 
                else:
                    return False
            result_array = self.merge_sort(A)
            print(result_array)
            return result_array
        else:
            return False
        
sol = Solution()
sol.sortedSquares([-4,-1,0,3,10])
