# Ask user for input
num = int(input("enter num: "))

# Open file in append mode so old content stays
with open("myfile.txt", "a") as f:   # add input with newline
    
    
    for i in range (11):
        t = (f"{num} x {i} = {i*num}")
        print(t)
        print(f.write(f"{t}\n"))
print("Your input has been saved!")
