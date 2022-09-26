tickets = [], parking_spaces = [], current_ticket = {'paid' : False}
class ParkingGarage:
    def init(self):
        self.tickets = [x for x in range(1,20)]
        self.parking_spaces = [x for x in range(1,20)]
        self.current_ticket = {}

    def takeTicket(self):
        print("Take your ticket.")
        print(f"\n{len(self.parking_spaces)} spots remaining")

        self.current_ticket = {'paid' : False}
        self.parking_spaces = self.parking_spaces[:-1]
        self.tickets = self.tickets[:-1]

    def pay(self):
        hours = input("How many hours have you been in the parking garage?")
        price = int(hours) * 3
        print(f"The total cost for parking is ${price}.")
        while True:
            payment = input("Would you like to pay? - yes/no ")


            if payment == 'yes':
                self.current_ticket = {'paid': True}
                price = int(hours) * 3
                print("." * 10)
                print("-~=        TICKET        =~-")
                print("\n" * 2)
                print(f"The total cost for parking is ${price}.")
                print("\nThank you for payment!")
                print("\n" * 2)
                print("." * 10)
                break

            elif payment == 'no':
                self.current_ticket = {'paid': False}
                print("Please pay your ticket to exit. ")
                continue

            else:
                self.current_ticket = {'paid': False}
                print("Please enter a valid payment ")

    def leave(self):
        if self.current_ticket == {'paid': False}:
            print('Please pay your ticket to exit. ')
            self.pay()

        elif self.current_ticket == {'paid': True}:

            for num in range(len(self.parking_spaces), 20):
                self.parking_spaces.append(num)
            for num in range(len(self.tickets), 20):
                self.tickets.append(num)
            print("Thank you! Have a nice day! ")



my_garage = ParkingGarage()

def run():
    while True:
        response = input("What would you like to do? enter/pay/spots/leave ")
        if response.lower() == 'enter':
            my_garage.takeTicket()

        elif response.lower() == 'pay':
            my_garage.pay()


        elif response.lower() == 'spots':
            print(f"{len(my_garage.parking_spaces)} spots remaining.")

        elif response.lower() == 'leave':
            my_garage.leave()
            break
        else:
            print("Invalid Entry.")

run() 
