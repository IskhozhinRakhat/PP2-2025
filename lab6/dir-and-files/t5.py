a = list(map(str,input().split()))
f = open("C:\Users\Рахат\Desktop\PP2-2025\1.txt.txt", "a")
for i in a:
    f.write(i+' ')
f.close()

f = open("C:\Users\Рахат\Desktop\PP2-2025\1.txt.txt", "r")
print(f.read())