nums=[1,2,3,2,5,4,2,1,6]
seen=set()
duplicates = set()
for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(list(duplicates))        

 