# def two_sum(nums, target):
#     seen={}
#     for i ,num in enumerate(nums):
#         complement= target-num
#         if complement in seen:
#             return[seen[complement],i]
#         seen[num]=i
# nums=list(map(int,input("Enter list of numbers:").split()))
# target=int(input("Enter a target number:"))        
        
# print(two_sum(nums,target))



def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
nums=[1,4,5,67,2,9]
target =10 
print(two_sum(nums, target))







def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
nums=[1,5,6,7,8,2]
target= 10   
print(two_sum(nums,target))         