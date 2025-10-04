import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

class TrainSystem:
    def __init__(self):
        self.trains = {
            "Rawapindi Express": {"Fare": 400, "ArrivalTime": 15, "From": "Rawalpindi", "To": "Lahore"},
            "Green line": {"Fare": 700, "ArrivalTime": 55, "From": "Rawalpindi", "To": "Swat"},
            "Shek Awan": {"Fare": 500, "ArrivalTime": 10, "From": "Rawalpindi", "To": "Karachi"},
            "king ways": {"Fare": 300, "ArrivalTime": 19, "From": "Rawalpindi", "To": "Kotli"},
        }

        # create folder and dump train details to a file
        os.makedirs("project1.py", exist_ok=True)
        file_path = os.path.join("project1.py", "train_detail.txt")
        with open(file_path, "w") as f:
            for tname, details in self.trains.items():
                f.write(f"train: {tname}\n")
                for k, v in details.items():
                    f.write(f"  {k}: {v}\n")
                f.write("\n")

    def show_status(self):
        # pick 2 random trains and set random seat counts
        self.name1, self.name2 = random.sample(list(self.trains.keys()), 2)
        self.seats1 = random.randint(20, 55)
        self.seats2 = random.randint(20, 55)
        self.fare1 = self.trains[self.name1]["Fare"]
        self.fare2 = self.trains[self.name2]["Fare"]

        print(Fore.GREEN + "--WELCOME--\n")
        print("If you want to check status enter 1 and for no enter 2")
        check_status = input("Enter (1 to view): ").strip()

        if check_status == "1":
            print(Fore.RED + f"EXPRESS TITLE\t: {self.name1}")
            print(Fore.GREEN + f"Seats Available\t: {self.seats1}")
            print(f"Ticket Price\t: {self.fare1}\n")

            print(Fore.RED + f"EXPRESS TITLE\t: {self.name2}")
            print(Fore.GREEN + f"Seats Available\t: {self.seats2}")
            print(f"Ticket Price\t: {self.fare2}\n")

            print("Do you want to book tickets? (1 for Yes, 2 for No)")
            try:
                seci = int(input("Enter : ").strip())
            except ValueError:
                print("Invalid input. Exiting.")
                return

            if seci == 1:
                # CALL the booking method (not define it here)
                self.book_tickets()
            else:
                print(Fore.LIGHTGREEN_EX + "Thanks for visiting")
        else:
            print(Fore.LIGHTGREEN_EX + "Thanks for visiting")

    def book_tickets(self):
        print(Fore.RED + f"If you want tickets for {self.name1} enter: 1")
        print(Fore.RED + f"If you want tickets for {self.name2} enter: 2")
        choice = input("Enter (1 or 2): ").strip()

        if choice == "1":
            train_name = self.name1
            available_seats = self.seats1
            fare = self.fare1
        elif choice == "2":
            train_name = self.name2
            available_seats = self.seats2
            fare = self.fare2
        else:
            print("Invalid choice. Returning to main.")
            return

        print(f"You chose: {train_name}")
        try:
            no_tickets = int(input(Fore.GREEN + "Please enter number of seats to book: ").strip())
        except ValueError:
            print("Invalid number. Booking cancelled.")
            return

        if no_tickets <= 0:
            print("Enter a positive number of tickets.")
            return

        if no_tickets > available_seats:
            print("Not enough seats available.")
            return

        total = no_tickets * fare
        print(f"Your total payment is: {total}")
        try:
            payment = int(input(f"Enter your payment amount (integer): ").strip())
        except ValueError:
            print("Invalid payment value. Payment denied.")
            return

        if payment >= total:
            print("✅ Payment approved. Booking confirmed!")
            change = payment - total
            if change > 0:
                print(Fore.RED + f"Your change is: {change}")

            # update available seats so next booking will reflect it
            if train_name == self.name1:
                self.seats1 -= no_tickets
            else:
                self.seats2 -= no_tickets

            # show minimal ticket info
            print(Style.RESET_ALL)
            print(f"Train: {train_name}")
            print(f"From: {self.trains[train_name]['From']}  To: {self.trains[train_name]['To']}")
            print(f"Seats booked: {no_tickets}  Remaining seats: {self.seats1 if train_name==self.name1 else self.seats2}")
        else:
            print("❌ Payment denied. Not enough money provided.")

if __name__ == "__main__":
    app = TrainSystem()
    app.show_status()
