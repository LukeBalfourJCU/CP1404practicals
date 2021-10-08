from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverService


def main():
    MENU = " (Q)uit \n (C)hoose taxi \n (D)rive"

    taxis = [Taxi("Prius 1", 200), SilverService("Limo", 300, 3), SilverService("Hummer", 500, 1.5)]
    current_taxi = None
    total_bill = 0

    print(MENU)
    user_select = input("\n").upper()

    while user_select != 'Q':
        if user_select == 'C':
            display_taxis(taxis)
            try:
                user_taxi = int(input("Choose taxi: ")) - 1
                current_taxi = taxis[user_taxi]
                print("You have chosen the {}".format(current_taxi.name))
            except IndexError:
                print("Please enter the number of a listed vehicle")

        elif user_select == 'D':
            if current_taxi:
                user_drive = int(input("Drive how far? "))
                current_taxi.drive(user_drive)
                print("You drive {}km".format(current_taxi.current_fare_distance))
                total_bill += current_taxi.get_fare()
            else:
                print("You need to chose a taxi before you can drive")

        else:
            print("Invalid Input")
        print("Bill: ${:.2f}".format(total_bill))
        print(MENU)
        user_select = input("\n").upper()



def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format((i + 1), taxi))


main()
