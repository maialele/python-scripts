def quick_sort(sequence):
    # check if the length of the item is less than one and if yes just return it
    length = len(sequence)
    if length <  1:
        return sequence
    # if not, pop the last item of the list and make it the index number (pivot number)
    else:
        pivot = sequence.pop()

    #make to lists, one is all the numbers that are greater than pivot and the other less than 
    items_greater = []
    items_lower = []

    # check every item in the list if its greater than the pivot or less than the pivot 
    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    # recursively return all of the lists and sublist created recurively
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([1,6,4,2,0,5,4,3]))