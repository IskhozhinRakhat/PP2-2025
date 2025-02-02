def uni(arr):
    l = []
    arr.sort()
    if(arr[0]!=arr[1]): l.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]: l.append(arr[i])
    return l

l = list(map(int,input().split()))
print(uni(l))