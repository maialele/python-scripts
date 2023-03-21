def largetst_sum(array):
    if len (array) == 0:
        return print('too small')

    max_sum = current_sum = array[0]

    for num in array[1:]:
        print("the number is: " + str(num))
        current_sum = max(current_sum + num, num)
        print("the current sum is: " + str(current_sum))
        max_sum = max(current_sum, max_sum)
        print("the max sum is: " + str(max_sum))

    return max_sum


print(largetst_sum([-12,-9,32,-13,10,2,-14,-7,-3]))
