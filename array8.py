# check if there is M and N elements such as N = 2 * M
# achar se um elemento é duas vezes o outro na lista
class Solution:
    def checkIfExist(self, arr: list) -> bool:
        if (len(arr) >= 2) and (len(arr) <= 500):
            for i in range(len(arr)):
                if (arr[i]*2) in arr[i+1:]:
                    return True
                elif (arr[i]/2) in arr[i+1:]:
                    return True
        return False
    