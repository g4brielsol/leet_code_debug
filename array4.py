# its not possible to change i in a for loop, use while instead

class Solution:
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if (len(arr) >= 1) and (len(arr) <= 10000):
            #                       doesnt go to the last one
            size = len(arr)
            number = 0
            while number < len(arr):
                if (arr[number] >= 0) and (arr[number] <= 9):
                    if arr[number] == 0:
                        arr = arr[0:number+1] + [0] + arr[number+1:]
                        arr = arr[0:size]
                        number += 1
                else:
                    return False
                number += 1
        else:
            return False
        print(arr)
        
        # output is the same length of input


        # input
        #[1,2,3,0,4,5,6,0,8,9]
        # output
        #[1,2,3,0,0,4,5,6,0,0]
        # input
        #[1,0,2,3]
        # output
        #[1,0,0,2]
        # input
        #[1,2,3]
        # output
        #[1,2,3]

solucao = Solution()
solucao.duplicateZeros([1,0,2,3,0,4,5,0])
#solucao.duplicateZeros([1,2,3])
        