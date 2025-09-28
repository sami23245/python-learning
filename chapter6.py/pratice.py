a = int(input("enter a num:-"))
b = int(input("enter a num:-"))
c = int(input("enter a num:-"))
e = int(input("enter a num:-"))

if(a>b):
    if(a>c):
        if(a>e):
            print("a id greater num")
        else:
            print("e is greater")
    elif(c>e):
        print("c is greater")
else:
    print("b is geater")


greatest = max(a, b, c, e)


print("The greatest number is:", greatest)