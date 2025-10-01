import random

class Train_tickets:
    def __init__(self, name , seats , fare ):
        self.name = name
        self.seats = seats
        self.fare = fare
        pass
    
status = Train_tickets("Pindi express" , 3 , 500 )

print(f"Express_title       : ", status.name)
print(f"Express_seats_status: ", status.seats)
print(f"Express_fare_price  : ", status.fare)

seat_num = random.randint(1, 30)
seat_num1 = random.randint(1, 30)
seat_num2 = random.randint(1, 30)

book_seats = int(input("enter number of seats you want to book: "))

print("fare price is 500 PKR")

fare = 500

payment = int(input("Enter your payment amount from below: "))

total_payment = 500 * book_seats

if book_seats <= 3:
    if payment == total_payment or payment > total_payment :
        
    
        print("payment approved")
        print("your seat numbers")
        if book_seats == 3:
            print(f"your seat number are {seat_num},{seat_num1},{seat_num2}")
            print("enjoy")
        elif book_seats == 2:
            print(f"your seat number are {seat_num},{seat_num1}")
            print("have a nice ride")
        else:
            print(f"your seat number are {seat_num}")
            print("my pleasure")
    else:
        print("ensuifcent payment")
else:
    print("not avaible seats")
    
if payment > total_payment:
    pay_back = payment - 500
    print(f"your returning payment is {pay_back}PKR")
    print("Glade to see you. May you have nice ride")
    
if book_seats <= 3:
    remaning_seates = 3 - book_seats
    
    
print(f"remaning seats -- {remaning_seates}")
print(f"fare price is ----{fare}")