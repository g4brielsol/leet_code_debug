# pay attention to range and array limits
# python doesnt care about function order
#class Solution:
#def merge_sort(self, array: list) -> list:
def merge_sort(array: list) -> list:
    if len(array) > 1:
        middle_index = len(array) // 2
        left = array[:middle_index]
        right = array[middle_index:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1
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
    
def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m, m+n):
        nums1[i] = nums2[i-m]
    nums1 = merge_sort(nums1)
    print(nums1)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3
#
#Output: [1,2,2,3,5,6]


#nums1 = [1,0], m = 1
#nums2 = [2],   n = 1
#
#Output: [1,2]
