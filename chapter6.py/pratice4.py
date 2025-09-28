print("Length ≥ 8/nContains at least one number/nContains at least one special character (!@#$%^&*)")


password = input("enter your password:")

if (password>=8 and password in (1,2,3,4,5,6,7,8,9,0) ):
    print("strong password")
else:
    print("weak password")