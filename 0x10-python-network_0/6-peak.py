#!/usr/bin/python3

def find_peak(list_of_integers):
    """finds a peak in a list of integers
    Args:
    list_of_integers: list of integers
    Returns:
    The index of the peak in the list"""

    if len(list_of_integers) <= 1:
        return None

    mid_index = len(list_of_integers) // 2

    if list_of_integers[mid_index - 1] < list_of_integers[mid_index] and \
            list_of_integers[mid_index + 1] < list_of_integers[mid_index]:
                return mid_index

    if list_of_integers[mid_index - 1] > list_of_integers[mid_index]:
        for i in range(mid_index - 1, -1, -1):
            if list_of_integers[i] > list_of_integers[mid_index] and list_of_integers[i] != list_of_integers[mid_index]:
                return i

    else:
        for i in range(mid_index + 1, len(list_of_integers)):
            if list_of_integers[i] > list_of_integers[mid_index] and list_of_integers[i] != list_of_integers[mid_index]:
                return i

    return None