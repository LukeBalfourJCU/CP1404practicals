from prac_08.silver_service_taxi import SilverService


def main():

    prius = SilverService("Prius 1", 200, 2)
    prius.start_fare()
    prius.drive(9)
    print(prius)
    print(prius.get_fare())
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print(prius.get_fare())


main()