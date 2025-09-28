with open("nothing.txt", "w") as f:
    f.write("Hello! This is my test file.")   # creates file and writes inside

with open("nothing.txt", "r") as f:
    t = f.read()
    print(t)


f = open("nothing.txt")

print(f.read())

f.close()