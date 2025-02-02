from itertools import permutations

def perm(s):
    for i in list(permutations(s)):
        print(i)
s = input()
print(perm(s))