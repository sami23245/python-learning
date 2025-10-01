class programmer(): #define class with name
    compyne = "microsoft"
    def __init__(self,name,salary,profession,pin): #
        self.name = name
        self.salary = salary
        self.profession = profession
        self.pin = pin
        
        
# name = int(input("enter your name: "))wrong code for now till 
# salary = int(input("enter your salary: "))
# profession = int(input("enter your profession: "))
# pin = int(input("enter your pin: "))


p = programmer("sami","1200k","data scyen",115544)


print(p.name,p.salary,p.profession,p.pin)