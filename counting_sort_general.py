# since it is not a comparing method, it must be different

def counting_sort(array:list) -> list:
    min_element = 0
    max_element = 0
    # find minimum element in array
    for number in array:
        if number < min_element:
            min_element = number

    # find biggest element in array
    for number in array:
        if number > max_element:
            max_element = number

    #range of values to be put in the counter list
    max_element = max_element - min_element

    # make list with max element length   
    count = [0 for i in range(max_element + 1)]
    # go through array indexes
    for i in array:
        # count how many times an element appears (if i == min_element -> is the first element of the array)
        count[i - min_element] +=  1
    
    #for all elements in array
    index = 0
    # loop how many elements can be (goes through a lot elements that count[i] == 0)
    # goes through all indexes that can be in max_element - min_element
    for i in range(max_element + 1):
        # enter for loop when the range(count[i]) is bigger than 0 
        # adds elements by index, ex: if index 0 has value of 3, means that are 3 elements
        # with the same value, considering the min value
        for j in range(count[i]):
            array[index] = i + min_element
            index += 1
    print(array)

counting_sort([3,2,1,0,10,13,2,14,25,2,3,1])