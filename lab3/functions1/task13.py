import random
def guess_the_number():
    x = random.randint(1,20)
    t = 0
    s = input("Hello! What is your name?\n")
    print(f"Well, {s}, I am thinking of a number between 1 and 20.")
    guess = int(input("Take a guess.\n"))
    while(guess != x):
        t+=1
        if guess < x: print("Your guess is too low.")
        else: print("Your guess is too high")
        guess = int(input("Take a guess.\n"))
    if guess == x: 
        print(f"Good job, {s}! You guessed my number in {t+1} guesses!")
    
#guess_the_number()