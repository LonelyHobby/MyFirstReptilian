def twoSum(self, nums, target):
    list=[0]*2
    for i in range(len(nums)+1): 
        for j in range(len(nums)+1):
            if (nums[i]+nums[j]==target):
                list=list+nums[i]
                list=list+nums[j]
                return list
nums=[2,7,11,15]
twoSum(nums,9)
