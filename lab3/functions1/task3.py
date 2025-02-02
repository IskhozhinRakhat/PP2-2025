def solve(numheads, numlegs):
    for i in range(1,numheads+1):
        if i*4+(numheads-i)*2==numlegs:
            return i, numheads-i
numheads = int(input())
numlegs = int(input())
rabbits, chickens = solve(numheads, numlegs)
print(f"count of rabbits : {rabbits}\ncount of chickens : {chickens}")