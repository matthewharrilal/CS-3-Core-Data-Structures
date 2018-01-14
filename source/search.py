#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests


    index_of_item = 0

    original_length = len(array)
    array_length = len(array)

    while array_length > 0:
        if array[index_of_item] == item:
            return  (array, index_of_item)
        if index_of_item > original_length:
            return None
        index_of_item += 1
        array_length -= 1
    return linear_search(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # So first we grab the length of the array 
    array_length = len(array)

    # This is what we are doing to handle if the user passes in an item that does not exist with in the list
    # of the array
    if index > array_length:
        return None

    # This is handling our base case or what we are trying to work towards
    if array[index] == item:
        # If we have found it then return the array subscripted at that index
        return array[index]

    # For both the base case as well as the error case we have to increment the count due to the reason
    # that if the item the user is looking for is not in the list then we increment the count because if it
    # is not there then the index would exceed the length of the list as well as for its in there we still have to
    #increment the count to go to the next element to see if it is in there
    return linear_search_recursive(array,item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # We have to sort the given array!
    sorted_array = sorted(array)

    len_of_sorted_array = len(sorted_array)


    left_bound = 0

    right_bound = len_of_sorted_array - 1

    print(sorted_array)

    if len_of_sorted_array == 0:
        return "Put some values in there homie"

    if item == sorted_array[left_bound]:
        return left_bound
    elif item == sorted_array[right_bound]:
        return right_bound

    while left_bound <= right_bound:
        middle_of_list = int((left_bound + right_bound) // 2)
        print("These are the middle of list %s" %(sorted_array[middle_of_list]))

        if item == sorted_array[middle_of_list]:
            return middle_of_list

        if item < sorted_array[middle_of_list]:
            right_bound = middle_of_list - 1

        if item > sorted_array[middle_of_list]:
            left_bound = middle_of_list + 1

    return binary_search_iterative(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    if left == None and right == None:
        left = 0
        right = len(array) - 1

    middle_of_list = (left + right) // 2

    if item == array[middle_of_list]:
        return middle_of_list
    
    if item < array[middle_of_list]:
        right = middle_of_list - 1
    
    if item > array[middle_of_list]:
        left = middle_of_list + 1

    if left > right:
        return None

    return binary_search_recursive(array, item, left, right)


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
