# check if array is a valid mountain (strict increase followed by strict decrease o values)
class Solution:
    def validMountainArray(self, A: list) -> bool:
        up = 0
        down = 0
        if len(A) >= 3:
            for i in range(1, len(A)):
                if A[i] > A[i-1]:
                    up = 1
                    if down == 1:
                        return False
                elif A[i] < A[i-1]:
                    down = 1
                    if (up == 0) and (down == 1):
                        return False
                else:
                    return False
            if (up == 1) and (down == 0):
                return False
            return True
            
        
       
    
    
        #[0,1,2,3,4,8,7,4,0] true
        #[0,1,1,2] false
        #[2,1] false
        #[0,1] false
        #[0,3,2,1] true
        
        #[0,3,2,3,1] true
        #[0,1,0] true
        #[4,3,2,1] false
        #[1,2,3,4] false
        #[]