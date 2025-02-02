def pall(s):
    return s == s[::-1]
s = input()
print(pall(s))