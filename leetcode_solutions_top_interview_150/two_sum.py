nums = [3,2,4]
target = 0


def TwoSum(nums,target):
    
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return [-1]


print(TwoSum(nums,target))