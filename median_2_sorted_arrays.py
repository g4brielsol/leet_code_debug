#Given two sorted arrays nums1 and nums2 of size m and n respectively,
#return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_list = sorted(nums1 + nums2)
        if len(total_list) == 0:
            return 0
        else:
            if len(total_list) == 1:
                return total_list[0]
            else:
                if len(total_list) % 2 == 0:
                    # pay attention to index -> it must be integer, not float
                    index = round(len(total_list)/2)
                    #print((total_list[index] + total_list[index - 1])/2)
                    return (total_list[index] + total_list[index - 1])/2
                else:
                    index = len(total_list)//2
                    return total_list[index]
        