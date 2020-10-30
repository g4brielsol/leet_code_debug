# Given an array arr, replace every element in that array with the greatest element 
# among the elements to its right, and replace the last element with -1.
# input = [17,18,5,4,6,1]
# output = [18,6,6,6,1,-1]

class Solution:
    def max_list_value(self, arr: list) -> int:
        max_value = 0
        for i in arr:
            if i > max_value:
                max_value = i
        
        return max_value
        
        
    def replaceElements(self, arr: list) -> list:
        if (len(arr) >= 1) and (len(arr) <= 10**4):
            #counter = 0
            size = len(arr)
            for i in range(0, size):
                arr[i] = self.max_list_value(arr[i+1:size])
            arr[-1] = -1
        
        return(arr)      
        
        
        #[1,2,5,4,3,0]
        #[5,2,5,4,3,0]
        #[5,5,5,4,3,0]
        #[5,5,4,4,3,0]
        #[5,5,4,3,3,0]
        #[5,5,4,3,0,0]
        #[5,5,4,3,0,-1]
        
        
        
        #[0,0,0]
        #[1,1,1,1]
        #[5,4,3,2,1]
        #[1,2,3,4,5]
        #[6,2,5,6,2,0]