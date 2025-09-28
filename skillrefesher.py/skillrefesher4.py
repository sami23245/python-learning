import random

n = random.randint(1,10)#use to gess num between 1 to 10

a = 0

while True :
    n2 = int(input("enter your number: "))
    
    a += 1
    
    if n > n2:
        print("too far")
    elif n < n2:
        print("not yet")
    else:
        print("yo bro you won")
    print(a)
    break