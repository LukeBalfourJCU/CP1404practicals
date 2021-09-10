from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print("{} ({}) : ${}".format(guitar.name, guitar.year, guitar.cost))
    print("{} ({}) : ${}".format(other.name, other.year, other.cost))
    print("For {} we expected 99 and got {}".format(guitar.name, guitar.get_age()))
    print("For {} we expected 9 and got {}".format(other.name, other.get_age()))
    print("{} is vintage = {}".format(guitar.name, guitar.is_vintage()))
    print("{} is vintage = {}".format(other.name, other.is_vintage()))


main()
