#Students are asked to stand in non-decreasing order of heights for an annual photo.

#Return the minimum number of students that must move in order for all students 
#to be standing in non-decreasing order of height.

#Notice that when a group of students is selected they can reorder in any 
#possible way between themselves and the non selected students remain on their seats.

# problem os sorting and comparing with sold list value

class Solution:
    def heightChecker(self, sizes: list) -> int:
        list_copy = list(sizes)
        if (len(sizes) >= 1) and (len(sizes) <= 100):
            min_value = sizes[0]
            max_value = sizes[-1]
            
            for element in sizes:
                if (element >= 1) and (element <= 100):
                    if element > max_value:
                        max_value = element
                    if element < min_value:
                        min_value = element
                else:
                    return -1
            
            max_value = max_value - min_value            #[1,1,2,3,4,5], 5-1 = 4
            counting = [0 for i in range(max_value + 1)] #0,1,2,3,4, 4 + 1 = 5
            
            for i in sizes:
                counting[i - min_value] += 1  #[2,1,1,1,1]
            # min_value = 1
            # max_value = 5
            # i - min_value -> counting index
            index = 0 
            #              [0,1,2,3,4]
            for i in range(max_value + 1):
                for j in range(counting[i]):
                    sizes[index] = i + min_value 
                    index += 1
        students_move = 0
        for i, j in zip(sizes, list_copy):
            if i != j:
                students_move += 1
            else:
                pass
        return students_move
                    
                                
            