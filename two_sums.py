


def twoSum(nums, target):
	for i in nums:
    	for j in nums:
        	j = j + 1
        	if target == nums[j] + nums[i]:
            	print ("the first index is: " + i + "and the second index is: " + j)
        	else:
            	continue


twoSum([1,2,3,4,5], 9)
