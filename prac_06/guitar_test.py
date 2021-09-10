from prac_06.Guitars import Guitar


def main():
    gibson = Guitar
    gibson.name = "Gibson L-5 CES"
    gibson.year = 1922
    gibson.cost = 16035.40
    print("{} ({}) : ${}".format(gibson.name, gibson.year, gibson.cost))

    print("{}".format(gibson.get_age(gibson.year)))


main()
