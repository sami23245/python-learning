import random
from colorama import Fore,Style
import os


print (Fore.GREEN + "--WECOME--")

print(Style.RESET_ALL)


class main:                     #this is main class in this contain every function
    
    def __init__(self):
        
        self.train = {
            "Rawapindi Express" :{"Fare" : 400,"ArivalTime" : 15 , "From" : "Rawalpindi" , "To" : "Lahore" } ,
            "Green line" : {"Fare" : 700, "ArivalTime" : 55 , "From" : "Rawalpindi" , "To" : "Swat" } ,
            "Shek Awan" :  {"Fare" : 500, "ArivalTime" : 10 , "From" : "Rawalpindi" , "To" : "karachi" } ,
            "king ways" : { "Fare" : 300, "ArivalTime" : 19 , "From" : "Rawalpindi" , "To" : "kotli" } ,
        }
        train = self.train
        
        file_path = os.path.join("project1.py", "train_detail.txt") #create file inside the project1.py folder
        os.makedirs("project1.py", exist_ok=True)
        
        with open (file_path,"w") as f: # put train data inside file 
            for train, details in train.items():
                f.write(f"train: {train}\n")
                for key, value in details.items():
                    f.write(f"  {key}:{value}\n")
                f.write("\n")
        
    def show_status(self):

        self.name1 , self.name2 = random.sample(list(self.train.keys()), 2)      #pick 2 from upper list

                                            #random sets
        self.seats1 = random.randint(20,55)
        self.fare1 = self.train[self.name1]

        self.seats2 = random.randint(20,55)
        self.fare2 = self.train[self.name2]
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
        
        def tickets_logic(self):
            if self.chec == "Train1":
                
                print(f"you chose {self.name1}")

                no_tickts = int(input(Fore.GREEN + "plzz no of seats you want to book :"))

                print(Style.RESET_ALL)

                if no_tickts <= self.seats1:
                
                    recipe = no_tickts * self.fare1
                
                    print(f"your total payment is {recipe}")
                    payment = str(input(f"enter your monet {recipe} "))
                
                    if payment == recipe or payment > recipe:
                    
                        print("your payment is aproved")
                        print("your seat num are")
                        user_return = recipe - payment
                        if user_return > 0 :
                            print(Fore.RED + f"your return is {user_return}")
                            # print(Style.RESET_ALL)
                            # print(Fore.GREEN + "")
                            # print (f"your train arive on{TODO} and depture on {todo}")
                            # print(f"your ticket is {to} to {from}")
                            # print(f"your seat number are {}")
                            # print(Style.RESET_ALL)
                        
                    else :
                    
                        print("payment denied")
            
status =  main()
status.show_status()
status.Book_tickets()