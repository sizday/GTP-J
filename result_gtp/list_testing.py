def same_first_last(nums):
    """Given an array of ints, return True if the array is length more than 1,
    and the first element and the last element are equal"""
    return len(nums) > 1 and nums[0] == nums[-1]


def sum_list_elem(list_data):
    """Find the sum of all elements of a list"""
    sum_list = []
    for x in list_data:
        sum_list.append(x)

    return sum(sum_list)


def sum_list_odd_position_elem(list_data):
    """Find the sum of the elements of a list in odd positions"""
    # A list is an ordered list, so the even positions of the list sum to 0
    # Find the sum of the odd positions of the list
    even_positions = []
    odd_positions = []
    for item in list_data:
        if item % 2!= 0:
            odd_positions.append(item)
        else:
            even_positions.append(item)
    return sum(odd_positions)


def reverse_list(list_data):
    """Reverse the list"""
    # this code is in the 'lst' module and I am calling it in the main module
    # here is how I am calling it
    print("In the main module")
    print(lst.reverse_list(list_data))
    print("\n")
    # this is what I want to do
    print(lst.reverse_list(list_data))
    print("\n")


def find_index_elem_in_list(elem, list_data):
    """Check if an element is in a list and return index"""
    return list_data.index(elem)


def join_lists(list1, list2):
    """Join 2 lists"""
    for i in range(len(list1)):
        list1[i] = list1[i].strip()
        list2[i] = list2[i].strip()
    return list1, list2


def sum_lists_by_elements(list1, list2):
    """Add the elements of two lists element by element and return the resulting list"""
    return [i + j for i in list1 for j in list2]


def sort_list(list_data):
    """Return sorted list"""

    list_data.sort()
    return list_data


def bubble_sort(list_data):
    """Return sorted list using bubble sort"""
    sorted_list = []
    for index, value in enumerate(list_data):
        if value < list_data[index-1]:
            sorted_list.append(value)
        else:
            sorted_list.append(list_data[index-1])
    return sorted_list


def are_elem_of_list_digits(list_data):
    """Check if all elements of a list are numbers"""
    if isinstance(list_data, list):
        for i in list_data:
            if not isinstance(i, int):
                return False
    return True


def maximum_difference(list_data):
    """Given a list, return the difference between the largest and smallest values"""
    max_value = 0
    min_value = 0
    for i in list_data:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    return max_value - min_value
