#!python
from binarytree import BinarySearchTree, BinaryTreeNode
import random
import pdb

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not

    counter = 0

    while counter < len(items) - 1:
        if items[counter] <= items[counter + 1]:
            counter += 1
            continue
        else:
            return False
    return True

def tree_sort(items):
    binary_tree = BinarySearchTree() # constant time
    for item in items: # n iterations
        binary_tree.insert(item) # O(n)
    print(binary_tree.items_in_order())
    binary_tree.items_in_order()


def update_pivot(items):
    pivot = random.choice(items)
    return pivot


def partition(items):
    # First we check if the list of items is already sorted
    if is_sorted(items) is True:
        return

    # This wall variable will stand as the cover for elements that have already been partitioned
    wall = -1

    pivot = len(items) - 1
    for index in range(len(items) - 1):
        if items[index] <= items[pivot]:
            wall += 1
            items[wall], items[index] = items[index], items[wall]

    temp = items[wall + 1]
    items[wall + 1] = pivot
    items[pivot], items[wall + 1] = temp, items[pivot]
    return items

def quicksort(items):
    # Now that we have the partitions function that arranges the left and right values based off of the pivot we have
    # to sort the items now

    if len(items) <= 2:
        return

    lesser_list = []
    greater_list = []
    pivot = 0

    for item in items[1:]:
        if item >= items[pivot]:
            lesser_list.append(item)
        elif item < items[pivot]:
            greater_list.append(item)
    quicksort(lesser_list)
    quicksort(greater_list)
    items[:] = greater_list + [items[pivot]] + lesser_list
    print(items)



def bubble_sort(items, order):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    # We are adding the order parameter that configures the result to acending or descending order

    counter = 0

    if is_sorted(items) is True:
        return items
    if order == 'ascending':

        while counter < len(items) - 1:
            if items[counter] <= items[counter + 1]:
                counter += 1
            else:
                items[counter + 1],items[counter] = items[counter], items[counter + 1]
                counter = 0
    elif order == 'descending':
        while counter < len(items) - 1:
            if items[counter] >= items[counter + 1]:
                counter += 1
            else:
                items[counter], items[counter + 1] = items[counter + 1],items[counter]
                counter = 0

    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    # Find minimum item in unsorted items
    # Swap it with first unsorted item
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
    # pdb.set_trace()

    if is_sorted(items) is True:
        return items

    while not is_sorted(items):
        for i in range(len(items) - 1):
            # setting the minimum to start with
            min = i
            # Start looping from the current index i
            for j in range(i + 1, len(items)):
                # if j is less than our current minimum
                if items[j] < items[min]:
                    # set j to our minimum
                    min = j
            # Once loop is done set i to be our minimum
            items[i], items[min] = items[min], items[i]
        return items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    # Repeat until all items are in sorted order
    # Take first unsorted item
    # Insert it in sorted order in front of items
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
    # NOTE: Need to be able to sort multiples

    if is_sorted(items) is True:
        return

    while not is_sorted(items):
        #
        for i in range(len(items)-1):
            # Loop through the list in reversal until you get to 0
            for j in range(i, - 1, -1):
                print(j)
                # If left index is bigger than right index
                if items[j] > items[j + 1]:
                    # Then swap
                    items[j], items[j + 1] = items[j + 1], items[j]
                else:
                    # Break once the item is not bigger and insert
                    break


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # The first step is to find the median of the list
    # DIVIDE: Split items list into approximately equal halves
    median = len(items) // 2
    first_half = items[:median]
    second_half = items[median:]

    # conquer: Sort each half using any other sorting algorithm
    sorted_first_half = first_half
    sorted_second_half = second_half
    insertion_sort(first_half)
    insertion_sort(second_half)

    # combine: Merge sorted halves into one list in sorted order
    # return merge(..., ...)
    sorted_list = []
    left_index = 0
    right_index = 0

    # Combine two sorted lists into one sorted list
    while left_index < len(sorted_first_half) and right_index < len(sorted_second_half):

        if sorted_first_half[left_index] < sorted_second_half[right_index]:
            sorted_list.append(sorted_first_half[left_index])
            left_index += 1

        else:
            sorted_list.append(sorted_second_half[right_index])
            right_index += 1

    while left_index < len(sorted_first_half):
        sorted_list.append(sorted_first_half[left_index])
        left_index += 1

    while right_index < len(sorted_second_half):
        sorted_list.append(sorted_second_half[right_index])
        right_index += 1
    items[:] = sorted_list
    print(items)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sorted_list = sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)





if __name__ == '__main__':
    main()
