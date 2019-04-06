
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    largest = int_list[0]
    for i in int_list:
        if i > largest:
            largest = i
    return largest


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return []

    last = int_list[len(int_list) - 1]
    int_list.remove(int_list[len(int_list) - 1])
    return [last] + reverse_rec(int_list)


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    if int_list == None:
        raise ValueError
    if int_list[low] == target:
        return low
    elif int_list[high] == target:
        return high
    if target < int_list[(low + high) // 2]:
        high = (low + high) // 2
    else:
        low = (low + high) // 2
    return bin_search(target, low, high, int_list)
