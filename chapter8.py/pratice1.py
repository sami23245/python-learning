def fun():
    m1 = int(input("enter num:-"))
    m2 = int(input("enter num:-"))
    m3 = int(input("enter num:-"))
    if (m1 > m2 and m1 > m3):
        print(f"the greater is {m1}")
    elif(m2 > m1 and m2 > m3):
        print(f"the greater is {m2}")
    else:
        print(f"the greater is {m3}")
        
fun()

def f_to_c():
    return 5*(f-32)/9

f = int(input("enter temp in F:"))
print(f_to_c(f))