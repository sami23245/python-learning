import random

# Random number between 1 and 10
n = random.randint(1, 10)

attempts = 0  # to count number of tries

while True:
    n2 = int(input("Enter your guess (1-10): "))
    attempts += 1
    
    if n2 < n:
        print("Too low! Try again.")
    elif n2 > n:
        print("Too high! Try again.")
    else:
        print(f"🎉 Yo bro you won in {attempts} tries!")
        break
