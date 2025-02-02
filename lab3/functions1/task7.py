def has_33(nums):
    for i in range(1,len(nums)):
        if(nums[i-1]==nums[i]==3): return True
    return False
l = list(map(int, input().split()))
print(has_33(l))