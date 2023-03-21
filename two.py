def twoSums(numbers, target):
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if i == j:
                continue
            result = numbers[i] + numbers[j]
            place_list = []
            if target == result:
                place_list.extend([i,j])
                return place_list
            else:
                continue

print(twoSums([2,5,5,11], 10))
