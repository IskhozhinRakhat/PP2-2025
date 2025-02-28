with open("C:\Users\Рахат\Desktop\PP2-2025\1.txt.txt",'r') as first, open("C:\Users\Рахат\Desktop\PP2-2025\2.txt.txt",'a') as second:
    for line in first:
        second.write(line)