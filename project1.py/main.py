import random
from colorama import Fore,Style


print (Fore.GREEN + "--WECOME--")

print(Style.RESET_ALL)


class main:                     #this is main class in this contain every function
    
    def __init__(self):
        self.train = ["Rawapindi Express","Green line","Shek Awan","king ways"]
        self.fares = [500,400,600,1000,350]
        
    def show_status(self):

        self.name1 , self.name2 = random.sample(self.train, 2)      #pick 2 from upper list

                                            #random sets
        self.seats1 = random.randint(20,55)
        self.fare1 = random.sample(self.fares, 1)

        self.seats2 = random.randint(20,55)
        self.fare2 = random.sample(self.fares, 1)
        a = "ststus"
        if a == "ststus":
            #for train one 
            print(Fore.RED + f"EXPRESS TITLE \t\t:{self.name1}")
            print(Fore.GREEN + f"NO of seats avaible \t:{self.seats1}")
            print(f"Ticket price \t\t:{self.fare1}")
            #for train two
            print(Fore.RED + f"EXPRESS TITLE \t\t:{self.name2}")
            print(Fore.GREEN + f"NO of seats avaible \t:{self.seats2}")
            print(f"Ticket price \t\t:{self.fare2}")
    def Book_tickets(self):
        
        
        print(Fore.RED + f"if you wnat to buy tickets for {self.name1} enter :Train1")
        print(Fore.RED + f"if you wnat to buy tickets for {self.name2} enter :Train2")
        
        print(Style.RESET_ALL)
        
        self.chec = str(input("Enter your choice: "))
        
        if self.chec == "Train1":
            print(f"you chose {self.name1}")
            no_tickts = int(input(Fore.GREEN + "plzz no of seats you want to book :"))
            print(Style.RESET_ALL)
            if no_tickts <= self.seats1:
                recipe = no_tickts * self.fare1
                print(f"your total payment is {recipe}")
                payment = str(input("enter your tx id "))
                if payment == payment:
                    print("your payment is aproved")
                    print("your seat num are")
                else :
                    print("payment denied")
            
status =  main()
status.show_status()
status.Book_tickets()