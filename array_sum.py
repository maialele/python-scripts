def array_sum(array, target):
    # if the array consists only of one number, stop
    if len(array) < 2:
        return print('too small')

    '''
    set two varibles, one for storing one number of the pair(because the loop have to run atleast twice) 
    and the other for presenting the output
    '''
    seen = set()
    output = set()

    # go through all the numbers in the array
    for number in array:
        # make a varible that stores the subtraction of the target number - the current number in the array. 
        sub = target - number

        # use the seen varible so we will not print the same pair twice
        if sub not in seen:
            seen.add(number)

        # if it is new, add it to the list get just two varibles in one way, so we will not get something like this (1,9) and (9,1)
        else:
            output.add((min(sub,number),max(sub,number)))

    return output

def find_sum_nums(array, target):
    # if the array consists only of one number, stop
    if len(array) < 2:
        return print('too small')

    output = set()

    for i in array:
        sub = target - i 

        if sub in array:
            if (sub,i) not in output and (i,sub) not in output:
                output.add((sub,i))
                print('({},{})'.format(sub, i))

        else:
            continue

array_sum([1,2,3,7,5,4,0,7,11,22,33], 12)

find_sum_nums([1,2,3,7,5,4,0,7,11,22,33], 12)

    
