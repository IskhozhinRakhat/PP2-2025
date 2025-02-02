def primes(array):
    l = []
    for i in range(len(array)):
        if(array[i] % 2 == 0): l.append(array[i])
    return l

l = list(map(int, input().split()))
print(primes(l))