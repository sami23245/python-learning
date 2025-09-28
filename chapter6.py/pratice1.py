m1 = float(input("enter your marks of math = "))
m2 = float(input("enter your marks of eng  = "))
m3 = float(input("enter your marks of urdu = "))
m4 = float(input("enter your marks of phy  = "))
m5 = float(input("enter your marks of com  = "))

total = m1 + m2 + m3 + m4 + m5

perstange = ((100*(total))/500)

if(perstange>=90):
    grade = "A+"
elif(perstange>80 and perstange<=89):
    grade = "B"
elif(perstange>70 and perstange<=69):
    grade = "C"
elif(perstange>60 and perstange<=69):
    grade = "D"
else:
    grade = "fail"
    
print("your" ,grade, "and your is " ,perstange, )