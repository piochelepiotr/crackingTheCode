def search_in_rotated_array(array, x):
    # let's assume element are distinct in the array for now
    # we can say that the array is composed of two sorted arrays, one after the other
    # the first element of the first array is bigger than all the elements of the second array
    in_first_array = x >= array[0]
    first = 0
    last = len(array)-1
    while last-first > 0:
        m = (last + first) // 2
        if array[m] >= array[0] and not in_first_array:
            # the element is after the end of the first array
            first = m+1
        elif array[m] < array[0] and in_first_array:
            last = m-1
        elif x >= array[m]:
            first = m
        else:
            last = m-1
    return last
