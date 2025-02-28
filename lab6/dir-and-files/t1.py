import os
path = 'D:\Steam'

print("Only directories:")
dirr = []
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path,i)):
        dirr.append(i)
print(dirr)

print("\nOnly files:")
ffiles = []
for i in os.listdir(path):
    if not os.path.isdir(os.path.join(path,i)):
        ffiles.append(i)
print(ffiles)

print("\nAll directories and files :")
all = []
for i in os.listdir(path):
    all.append(i)
print(all)