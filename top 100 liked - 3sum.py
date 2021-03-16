# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: list) -> list:
        if len(nums) == 0:
            return []
        else:
            answer_list = []
            #nums.sort()
            for index_1 in range(0, len(nums)):
                for index_2 in range(0, len(nums)):
                    for index_3 in range(0, len(nums)):
                        if (index_1 == index_2) or (index_1 == index_3) or (index_2 == index_3) :
                            continue
                        else:
                            three_element_sum = nums[index_1] + nums[index_2] + nums[index_3]  
                            if three_element_sum == 0:
                                three_elements = sorted([nums[index_1], nums[index_2],nums[index_3]])
                                if three_elements not in answer_list:
                                    answer_list.append(three_elements)
        #    pre_final_list = []
        #    for element in answer_list:
        #        pre_final_list.append(sorted(element))

        #    final_list = []
        #    for index_1 in range(0, len(pre_final_list)):
        #        for index_2 in range(0, len(pre_final_list)):
        #            if index_1 != index_2:
        #                if pre_final_list[index_2] not in final_list:
        #                    final_list.append(pre_final_list[index_2])
            return answer_list
            
                        
            
        