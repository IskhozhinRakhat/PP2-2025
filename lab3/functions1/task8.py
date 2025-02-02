def spy_game(nums):
    zero = seven = 0
    for i in range(len(nums)):
        if nums[i] == 0: zero += 1
        elif nums[i] == 7: seven += 1
        if zero == 2 and seven == 1:
            return True
    return False

l = list(map(int, input().split()))
print(spy_game(l)) 