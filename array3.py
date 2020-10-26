class Solution:
    def merge_sort(self, array: list) -> list:
        """ Implementation of merge sort """
        if len(array) > 1:
            # find middle (int)
            middle = len(array) // 2
            # two arrays divided in the middle index
            left = array[:middle]
            right = array[middle:]
            # recursion 
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
            # get less value and put in first order
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            
            # check if any value was left while the other array has already finished
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
        """ Square arrays and call merge sort """
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
